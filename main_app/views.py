from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blogpost, Comment
from .forms import CommentForm, BlogpostForm
from django.urls import reverse


# all views below
class BlogpostUpdate(UpdateView):
    model = Blogpost
    fields = ['title', 'category', 'context']
    success_url = '/blogposts/{id}'

class BlogpostDelete(DeleteView):
    model = Blogpost
    success_url = '/blogposts'

class BlogpostCreate(CreateView):
    model = Blogpost
    fields = ['title', 'category', 'context', 'cooking_time']
    success_url = '/blogposts/'

def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# view all blog post page "foodie Tribe Blog Post"
def blogposts_index(request):
    blogposts = Blogpost.objects.all()
    return render(request, 'blogposts/index.html', {'blogposts': blogposts})

# view for displaying the details of a specific blog post 
def blogposts_detail(request, blogpost_id):
    blogpost = get_object_or_404(Blogpost, id=blogpost_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blogpost = blogpost
            comment.save()
            return redirect('detail', blogpost_id=blogpost_id)  
    else: 
        form = CommentForm()

    # comments associated with the current blog post
    comments = Comment.objects.filter(blogpost=blogpost)

    return render(request, 'blogposts/detail.html', { 'blogpost': blogpost, 'form': form, 'comments': comments})


# comment submissions
def comment(request, blogpost_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blogpost_id = blogpost_id
            new_comment.category = Blogpost.objects.get(pk=blogpost_id).category
            new_comment.save()
            return redirect('detail', blogpost_id=blogpost_id)
    else: 
        form = CommentForm()
    return render(request, 'blogposts/detail.html', {'form': form})
