from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Blogpost(models.Model):
    CATEGORY_CHOICES = (
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('pescatarian', 'Pescatarian'),
        ('halal', 'Halal'),
        ('kosher', 'Kosher'),
        ('sugarfree', 'Sugar Free'),
        ('glutenfree', 'Gluten Free'),
        ('dairyfree', 'Dairy Free'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(
        max_length=15, 
        choices=CATEGORY_CHOICES,
        default=CATEGORY_CHOICES[0][0] 
    )
    context = models.CharField(max_length=500)
    cooking_time = models.IntegerField(default=0)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f'Comment on {self.blogpost.title} at {self.created_at}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'blogpost_id': self.blogpost_id})
