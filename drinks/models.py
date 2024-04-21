from django.db import models

# Create your models here.
class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    Drink_Choices = [
        ('coffee', 'Coffee'),
        ('non_coffee', 'Non Coffee'),
    ]
    merchant_area = models.CharField(max_length=255)
    merchant_name = models.CharField(max_length=255)
    category = models.CharField(max_length=13, choices=Drink_Choices)
    product = models.CharField(max_length=255)
    description = models.CharField(max_length=255)