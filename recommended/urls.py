from django.urls import path
from recommended.views import show_page, show_json

app_name = 'recommended'

urlpatterns = [
    path('', show_page, name='show_page'),
    path("show_json/", show_json, name="show_json")

]