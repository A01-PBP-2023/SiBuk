from django.urls import path
from .views import review_FnD, get_reviews_json

app_name = "reviews"

urlpatterns = [
    path('review_fnd', review_FnD, name='review_fnd'),
    path('get_reviews_json', get_reviews_json, name='get_reviews_json')
]