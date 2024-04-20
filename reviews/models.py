from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Review(models.Model):
    rating = models.IntegerField()
    ulasan = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
>>>>>>> origin/main
