from django import forms
from .models import Post, Rating

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body',)

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('value',)
