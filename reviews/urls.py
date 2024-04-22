from django.urls import path
from .views import review_FnD, get_reviews_json, get_reviews_template

app_name = "reviews"

urlpatterns = [
    path('review_fnd', review_FnD, name='review_fnd'),
    path('get_reviews_json', get_reviews_json, name='get_reviews_json'),
    path('get_reviews_template', get_reviews_template, name='get_reviews_template'),
]