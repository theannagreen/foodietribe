from django.db import models
from django.urls import reverse


# Create your models here.
class Comment(models.Model):
    blogpost = models.ForeignKey('Blogpost', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

def __str__(self):
    return f'Comment on {self.blogpost.title} at {self.created_at}'
    
class Blogpost(models.Model):
    CATEGORY_CHOICES = [
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('pescatarian', 'Pescatarian'),
        ('halal', 'Halal'),
        ('kosher', 'Kosher'),
        ('sugarfree', 'Sugar Free'),
        ('glutenfree', 'Gluten Free'),
        ('dairyfree', 'Dairy Free'),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    context = models.CharField(max_length=500)

def __str__(self):
    return self.title
    
def get_absolute_url(self):
    return reverse('detail', kwargs={'blogpost_id': self.id})