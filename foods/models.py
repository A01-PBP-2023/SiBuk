from django.db import models

# Create your models here.
class Food(models.Model):
    id = models.AutoField(primary_key=True)
    FOOD_CHOICES = [
        ('nasi', 'Nasi'),
        ('snack', 'Snack'),
        ('mie', 'Mie'),
        ('lainnya', 'Lainnya')
    ]
    merchant_area = models.CharField(max_length=255)
    merchant_name = models.CharField(max_length=255)
    category = models.CharField(max_length=13, choices=FOOD_CHOICES)
    product = models.CharField(max_length=255)
    description = models.CharField(max_length=255)