from django.db import models
from django.db.models.fields import CharField, DateField, TextField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Term(models.Model):
    title = CharField(max_length=120)
    defn = TextField()
    
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = CharField(max_length=120)
    blog = TextField()
    date = DateField(default= timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title