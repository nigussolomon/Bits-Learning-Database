from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Term, Blog

# Create your views here.

@login_required
def home_database(request):
    return render(request, 'database/home.html')

@login_required
def blog_database(request):
    context = {
        'blog' : Blog.objects.all(),
        'title':'BLOG'
    }
    return render(request, 'database/blog.html', context)

@login_required
def terms(request):
    context = {
        'data': Term.objects.all()
    }
    
    return render(request, 'data/CS/terms.html', context)




