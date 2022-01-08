from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models.base import Model
from django.forms import fields
from django.forms.models import ModelForm
from database.models import Blog, BugReport


class Registration(UserCreationForm):
    email = forms.EmailField(max_length=180, required=True)

    def clean_email(self):
        data = self.cleaned_data['email']
        if "@bitscollege.edu.et" not in data:   # any check you need
            raise forms.ValidationError("Please use the email given to you by bits")
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'This is email is already in use if your email was used by someone else please contact the school')
        return email
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'blog']

class ContactForm(ModelForm):

    class Meta:
        model = BugReport
        fields = ['bug', 'bug_detail']