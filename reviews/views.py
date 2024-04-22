from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse

from .models import Review
from .forms import ReviewForm
from foods.models import Food
# from drinks.models import Drink

@login_required(login_url='/user_auth/login')
def review_FnD(request, content_type, object_id):
    content_type = ContentType.objects.get(model=content_type)
    if content_type.model == 'food':
        obj = get_object_or_404(Food, pk=object_id)
    # elif content_type.model == 'drink':
    #     obj = get_object_or_404(Drink, pk=object_id)
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
            return HttpResponseRedirect(reverse('drinks:main')) # Change this
    form = ReviewForm()
    return render(request, 'review_form.html', {'object': obj, 'form':form})

def get_reviews_json(request, content_type, object_id):
    content_type = ContentType.objects.get(model=content_type)
    if content_type.model == 'food':
        obj = get_object_or_404(Food, pk=object_id)
    # elif content_type.model == 'drink':
    #     obj = get_object_or_404(Drink, pk=object_id)
    else:
        return HttpResponseBadRequest("Invalid content type")
    reviews = Review.objects.filter(content_type=content_type, object_id=object_id)
    reviews_data = serializers.serialize('json', reviews)
    return JsonResponse({'reviews': reviews_data}, safe=False)

def get_reviews_template(request, content_type, object_id):
    content_type = ContentType.objects.get(model=content_type)
    if content_type.model == 'food':
        obj = get_object_or_404(Food, pk=object_id)
    # elif content_type.model == 'drink':
    #     obj = get_object_or_404(Drink, pk=object_id)
    else:
        return HttpResponseBadRequest("Invalid content type")
    reviews = Review.objects.filter(content_type=content_type, object_id=object_id)
    return render(request, 'fnd_reviews.html', {'reviews': reviews})