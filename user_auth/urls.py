from django.urls import path
from .views import register, login_user, logout_user

app_name = "user_auth"

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]