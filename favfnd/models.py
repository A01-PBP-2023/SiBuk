from django.db import models
from django.contrib.auth.models import User
from foods.models import Food 
# Create your models here.
class Favorite(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ManyToManyField(Food)

