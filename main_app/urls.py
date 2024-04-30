from django.urls import path
from . import views
	

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogposts/', views.blogposts_index, name='index'),
    path('blogposts/<int:blogpost_id>/', views.blogposts_detail, name='detail'),
    path('blogposts/create/', views.BlogpostCreate.as_view(), name='create'),
    path('blogposts/update/<int:pk>', views.BlogpostUpdate.as_view(), name='update'),
    path('blogposts/delete/<int:pk>', views.BlogpostDelete.as_view(), name='delete'),
    path('blogposts/<int:blogpost_id>/new_comment/', views.comment, name='new_comment'),
]
 