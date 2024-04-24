from django.urls import path
from favfnd.views import show_favorites

app_name = 'favfnd'

urlpatterns = [
    path('', show_favorites, name='show_favorites'),
]