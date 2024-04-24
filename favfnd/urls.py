from django.urls import path
from favfnd.views import show_favorites, show_json, show_all_attributes

app_name = 'favfnd'

urlpatterns = [
    path('', show_favorites, name='show_favorites'),
    path('show_json/', show_json, name='show_json'),
    path("show_all_attributes/", show_all_attributes, name="show_all_attributes")
]