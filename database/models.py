from django.db import models
from django.db.models.fields import CharField, DateField, TextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class TermCs(models.Model):
    title = CharField(max_length=120, default="please enter the title")
    defn = TextField(default="please enter the details")
    
    def __str__(self):
        return self.title



class TermSe(models.Model):
    title = CharField(max_length=120, default="please enter the title")
    defn = TextField(default="please enter the details")
    
    def __str__(self):
        return self.title


    
class Blog(models.Model):
    title = CharField(default = "Enter your title", max_length=120)
    blog = TextField(default = "Enter your Blog")
    date = models.DateTimeField(default= timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date',]
    
    def __str__(self):
        return self.title

class BugReport(models.Model):
    bug = CharField(max_length=300, default="What problems did you encounter")
    bug_detail = TextField(default="Tell us detail about your problem so that we can help you more")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return self.bug