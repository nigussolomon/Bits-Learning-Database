from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models.base import Model
from django.forms import fields
from django.forms.models import ModelForm
from database.models import Blog


class Registration(UserCreationForm):
    email = forms.EmailField(max_length=180, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'blog']

class TestForm(ModelForm):
     
     class Meta:
         model = Blog
         fields = ['title','blog']