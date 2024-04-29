from django.db import models
from django.urls import reverse


# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    context = models.CharField(max_length=500)


def __str__(self):
    return self.name
    
def get_absolute_url(self):
    return reverse('detail', kwargs={'blogposts_id': self.id})
