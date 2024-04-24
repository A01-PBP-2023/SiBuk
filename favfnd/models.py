from django.db import models
from django.contrib.auth.models import User
from foods.models import Food 


class Favorite(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favfood = models.ManyToManyField(Food)

