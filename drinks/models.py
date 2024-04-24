from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from reviews.models import Review

# Create your models here.
class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    DRINK_CHOICES = [
        ('kopi', 'Kopi'),
        ('non kopi', 'Non kopi')
    ]
    merchant_area = models.CharField(max_length=255)
    merchant_name = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    category = models.CharField(max_length=13, choices=DRINK_CHOICES)
    description = models.CharField(max_length=255)
    reviews = GenericRelation(Review)