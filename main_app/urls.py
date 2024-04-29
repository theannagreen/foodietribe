from django.urls import path
from . import views
	

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogposts/', views.blogposts_index, name='index'),
    path('blogposts/<int:blogpost_id>/', views.blogposts_detail, name='detail'),
]
