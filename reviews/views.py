from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse
from django.db.models import Count, Avg
from django.template.loader import render_to_string

from .models import Review
from .forms import ReviewForm
from foods.models import Food
from drinks.models import Drink

@login_required(login_url='/user_auth/login')
def review_FnD(request, content_type, object_id):
    content_type = ContentType.objects.get(model=content_type)
    if content_type.model == 'food':
        obj = get_object_or_404(Food, pk=object_id)
    elif content_type.model == 'drink':
        obj = get_object_or_404(Drink, pk=object_id)
    else:
        return HttpResponseBadRequest("Invalid content type")

    if request.method == 'POST':
        rating = request.POST.get('rating')
        ulasan = request.POST.get('ulasan')
        Review.objects.create(
            user = request.user,
            rating=rating,
            ulasan=ulasan,
            content_type=content_type,
            object_id=object_id
        )
        if content_type.model == 'food':
            return HttpResponseRedirect(reverse('foods:show_food'))
        else:
            return HttpResponseRedirect(reverse('drinks:main'))
    form = ReviewForm()
    return render(request, 'review_form.html', {'object': obj, 'form':form})

def get_reviews_json(request, content_type, object_id):
    content_type = ContentType.objects.get(model=content_type)
    if content_type.model == 'food':
        obj = get_object_or_404(Food, pk=object_id)
    elif content_type.model == 'drink':
        obj = get_object_or_404(Drink, pk=object_id)
    else:
        return HttpResponseBadRequest("Invalid content type")
    reviews = Review.objects.filter(content_type=content_type, object_id=object_id)
    reviews_data = serializers.serialize('json', reviews)
    return JsonResponse({'reviews': reviews_data}, safe=False)

def get_reviews_template(request, content_type, object_id):
    content_type = ContentType.objects.get(model=content_type)
    if content_type.model == 'food':
        obj = get_object_or_404(Food, pk=object_id)
    elif content_type.model == 'drink':
        obj = get_object_or_404(Drink, pk=object_id)
    else:
        return HttpResponseBadRequest("Invalid content type")
    reviews = Review.objects.filter(content_type=content_type, object_id=object_id)
    return render(request, 'fnd_reviews.html', {'reviews': reviews})

def reviews_template(request):
    return render(request, 'all_reviews.html')

def get_all_reviews_partial(request):
    data = []

    foods = Food.objects.prefetch_related('reviews').annotate(num_reviews=Count('reviews')).all()
    for food in foods:
        food_data = serializers.serialize('python', [food])[0]
        food_data['type'] = 'food'
        food_data['fields']['average_rating'] = food.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
        food_data['fields']['percentage_rating'] = food_data['fields']['average_rating']/5*100
        food_data['fields']['num_reviews'] = food.num_reviews
        data.append(food_data)

    drinks = Drink.objects.prefetch_related('reviews').annotate(num_reviews=Count('reviews')).all()
    for drink in drinks:
        drink_data = serializers.serialize('python', [drink])[0]
        drink_data['type'] = 'drink'
        drink_data['fields']['average_rating'] = drink.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
        drink_data['fields']['percentage_rating'] = drink_data['fields']['average_rating']/5*100
        drink_data['fields']['num_reviews'] = drink.num_reviews
        data.append(drink_data)

    sort_by = request.GET.get('sort_by')
    if sort_by == 'rating':
        data.sort(key=lambda x: x['fields']['average_rating'] or 0, reverse=True)
    elif sort_by == 'reviews':
        data.sort(key=lambda x: x['fields']['num_reviews'], reverse=True)

    # Render the template with the data
    html_content = render_to_string('partial_all_reviews.html', {'data': data})

    return JsonResponse({'html_content': html_content})