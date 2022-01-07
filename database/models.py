from django.db import models
from django.db.models.fields import CharField, DateField, TextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Term(models.Model):
    title = CharField(max_length=120)
    defn = TextField()
    
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = CharField(default = "Enter your title", max_length=120)
    blog = TextField(default = "Enter your Blog")
    date = DateField(default= timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blogdatabase', kwargs={'pk': self.pk})