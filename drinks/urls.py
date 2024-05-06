from django.urls import path
from .views import show_drink, drink_detail, add_drink, get_drink, get_drink_by_id, filter_drink, add_to_favorites

app_name = 'drinks'

urlpatterns = [
    path('', show_drink, name='show_drink'),
    path('drink_detail/<int:drink_id>/', drink_detail, name='drink_detail'),
    path('add_drink/', add_drink, name='add_drink'),
    path('get_drink/', get_drink, name='get_drink'),
    path('get_drink/<int:id>/', get_drink_by_id, name="get_drink_by_id"),
    path('filter_drink/', filter_drink, name='filter_drink'),
    path('add_to_favorites/', add_to_favorites, name='add_to_favorites'),
]