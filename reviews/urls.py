from django.urls import path
from .views import review_FnD, get_reviews_json, get_reviews_template, reviews_template, get_all_reviews_partial

app_name = "reviews"

urlpatterns = [
    path('get_template', reviews_template, name='get_template'),
    path('get_reviews_template', get_all_reviews_partial, name='get_reviews_template'),
    path('<str:content_type>/<int:object_id>/review_fnd', review_FnD, name='review_fnd'),
    path('<str:content_type>/<int:object_id>/get_reviews_json', get_reviews_json, name='get_reviews_json'),
    path('<str:content_type>/<int:object_id>/get_reviews_template', get_reviews_template, name='get_reviews_template'),
]