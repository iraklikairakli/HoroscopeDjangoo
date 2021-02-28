from django import forms
from .models import Blogmodel

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogmodel
        fields = [
            'Title',
            'body',
            'slug',
            'tags'
        ]