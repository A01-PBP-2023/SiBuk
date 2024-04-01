from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType

from .models import Review
from foods.models import Foods
from drinks.models import Drinks

def review_FnD(request, content_type_id, object_id):
    # Get the content type and object based on IDs
    content_type = get_object_or_404(ContentType, pk=content_type_id)
    if content_type.model == 'food':
        obj = get_object_or_404(Foods, pk=object_id)
    elif content_type.model == 'drink':
        obj = get_object_or_404(Drinks, pk=object_id)
    else:
        return HttpResponseBadRequest("Invalid content type")

    if request.method == 'POST':
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        review = Review.objects.create(
            rating=rating,
            review=review,
            content_type=content_type,
            object_id=object_id
        )
        return HttpResponseRedirect('/')
    
    return render(request, 'review_form.html', {'object': obj})