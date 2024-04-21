from django.db import models

# Create your models here.
class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    DRINK_CHOICES = [
        ('kopi', 'Kopi'),
        ('non kopi', 'Non kopi')
    ]
    merchant_area = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=13, choices=DRINK_CHOICES)
    product_description = models.CharField(max_length=255)
    image = models.URLField()