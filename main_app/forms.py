from django import forms
from django.forms import ModelForm
from .models import Blogpost, Comment

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'category', 'context']
        widgets = {
            'category': forms.Select(choices=Blogpost.CATEGORY_CHOICES),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
