from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    context = models.CharField(max_length=500)