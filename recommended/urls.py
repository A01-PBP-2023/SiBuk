from django.urls import path
from recommended.views import show_page

app_name = 'recommended'

urlpatterns = [
    path('', show_page, name='show_page'),
]