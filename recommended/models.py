from django.db import models

# Create your models here.
class Recommended(models.Model) :
   merchant_name = models.TextField(null=True, blank=True)
   merchant_area = models.TextField(null=True, blank=True)
   category = models.TextField(null=True, blank=True)
   display = models.TextField(null=True, blank=True)
   product = models.TextField(null=True, blank=True)
   price = models.IntegerField(null=True, blank=True)
   discount_price = models.IntegerField(null=True, blank=True)
   isDiscount = models.IntegerField(null=True, blank=True)
   description = models.TextField(null=True, blank=True)
