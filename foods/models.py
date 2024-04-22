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
    merchant_area = models.CharField(max_length=255, null=True, blank=True)
    merchant_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=13, choices=FOOD_CHOICES, null=True, blank=True)
    product = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)