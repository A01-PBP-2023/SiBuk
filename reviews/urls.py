from django.urls import path
from .views import review_FnD

app_name = "reviews"

urlpatterns = [
    path('', review_FnD, name='review_FnD'),
]