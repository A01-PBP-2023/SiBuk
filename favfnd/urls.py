from django.urls import path
from favfnd.views import show_favorites, show_json_favfood, show_favfood, show_favdrink, filter_foods, filter_drink

app_name = 'favfnd'

urlpatterns = [
    path('', show_favorites, name='show_favorites'),
    path("food/", show_favfood, name="show_favfood"),
    path('food/filter_foods/', filter_foods, name='filter_foods'),
    path("drink/", show_favdrink, name="show_favdrink"),
    path('drink/filter_drink/', filter_drink, name='filter_drink'),
    path("json/", show_json_favfood, name="show_json_favfood"),
]
