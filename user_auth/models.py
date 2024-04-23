from django.db import models
from django.contrib.auth.models import User
from foods.models import Food

class UserProfile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10)
    favorite_food = models.ManyToManyField(Food, related_name="favorite_food")