from django.db import models

# Create your models here.
class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    Drink_Choices = [
        ('coffee', 'Coffee'),
        ('non_coffee', 'Non Coffee'),
    ]
    Merchant_area = models.CharField(max_length=255)
    Product_name = models.CharField(max_length=255)
    Category = models.CharField(max_length=13, choices=Drink_Choices)
    Product_description = models.CharField(max_length=255)
    Image = models.URLField()