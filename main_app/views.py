from django.shortcuts import render

mainblogs = [
  {'name': 'Lolo', 'category': 'vegan', 'description': 'crispy tofu is life changing'},
]
# Create your views here.
def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# this shows the view all blog post page "foodie Tribe Blog Post"
def mainblog_index(request):
  return render(request, 'mainblog/index.html', {
    'mainblogs': mainblogs
  })