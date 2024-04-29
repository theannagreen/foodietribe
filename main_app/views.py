from django.shortcuts import render
from .models import Blogpost

blogposts = [
  {'name': 'Lolo', 'category': 'vegan', 'description': 'crispy tofu is life changing'},
]
# Create your views here.
def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# this shows the view all blog post page "foodie Tribe Blog Post"
def blogposts_index(request):
    blogposts = Blogpost.objects.all()
    return render(request, 'blogposts/index.html', {'blogposts': blogposts})

# This shows the view for displaying the details of a specific blog post 
def blogposts_detail(request, blogpost_id):
   blogpost = Blogpost.objects.get(id=blogpost_id)
   return render(request, 'blogposts/detail.html', { 'blogpost': blogpost})