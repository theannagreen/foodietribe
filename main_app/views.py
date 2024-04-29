from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blogpost, Comment
from .forms import CommentForm

# Create your views here.

class BlogpostUpdate(UpdateView):
    model = Blogpost
    fields = ['title', 'category', 'context']
    success_url = '/blogposts/{id}'

class BlogpostDelete(DeleteView):
    model = Blogpost
    success_url = '/blogposts'

class BlogpostCreate(CreateView):
    model = Blogpost
    fields = '__all__'
    success_url = '/blogposts/{id}'

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
   blogpost = get_object_or_404(Blogpost, id=blogpost_id)
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.blogpost = blogpost
           comment.save()
           return redirect('blogposts_detail', blogpost_id=blogpost_id)
   else: 
       form = CommentForm()
   return render(request, 'blogposts/detail.html', { 'blogpost': blogpost, 'form': form})
