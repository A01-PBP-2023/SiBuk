from django.db import models

# Create your models here.
class Foods(models.Model):
    id = models.AutoField(primary_key=True)
    FOOD_CHOICES = [
        ('asam', 'Asam'),
        ('manis', 'Manis'),
        ('gurih', 'Gurih'),
    ]
    Merchant_area = models.CharField(max_length=255)
    Product_name = models.CharField(max_length=255)
    Category = models.CharField(max_length=13, choices=FOOD_CHOICES)
    Product_description = models.CharField(max_length=255)
    Image = models.URLField()