from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.core import serializers
from django.urls import reverse

# from .models import Review
# from foods.models import Foods # Change this
# from drinks.models import Drinks # Change this

# def review_FnD(request, content_type_id, object_id):
#     # Get the content type and object based on IDs
#     content_type = get_object_or_404(ContentType, pk=content_type_id)
#     if content_type.model == 'foods':
#         obj = get_object_or_404(Foods, pk=object_id)
#     elif content_type.model == 'drinks':
#         obj = get_object_or_404(Drinks, pk=object_id)
#     else:
#         return HttpResponseBadRequest("Invalid content type")

#     if request.method == 'POST':
#         rating = request.POST.get('rating')
#         review = request.POST.get('review')
#         review = Review.objects.create(
#             rating=rating,
#             review=review,
#             content_type=content_type,
#             object_id=object_id
#         )
#         if content_type.model == 'foods':
#             return HttpResponseRedirect(reverse('foods:main')) # Change this
#         else:
#             return HttpResponseRedirect(reverse('drinks:main')) # Change this
        
#     return render(request, 'review_form.html', {'object': obj})

# def get_reviews_json(request, content_type_id, object_id):
#     content_type = get_object_or_404(ContentType, pk=content_type_id)
#     if (content_type.model != 'foods') or (content_type.model != 'drinks'):
#         return HttpResponseBadRequest("Invalid content type")
#     reviews = Review.objects.filter(content_type=content_type, object_id=object_id)
#     reviews_data = serializers.serialize('json', reviews)
#     return JsonResponse({'reviews': reviews_data}, safe=False)