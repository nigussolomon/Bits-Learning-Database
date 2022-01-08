from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . models import TermCs, Blog, TermSe
from django.contrib.auth.models import User
from  main.forms import BlogForm

# Create your views here.

@login_required
def home_database(request):
    return render(request, 'database/home.html')

@login_required
def blog_database(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            form.cleaned_data
            return redirect('blogdatabase')
    else:
        form = BlogForm(instance = request.user)

    context = {
        'blog' : Blog.objects.all().order_by('-date'),
        'title':'BLOG',
        'form':form
    }
    return render(request, 'database/blog.html', context)

@login_required
def termscs(request):
    context = {
        'datacs': TermCs.objects.all()
    }
    
    return render(request, 'data/CS/terms.html', context)


def termsse(request):
    context = {
        'datase': TermSe.objects.all()
    }
    
    return render(request, 'data/SE/terms.html', context)




