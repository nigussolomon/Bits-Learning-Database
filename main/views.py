from django.shortcuts import redirect, render
from . forms import Registration
from database.models import Blog

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def blog(request):
    context = {
        'blog': Blog.objects.all(),
        'title': 'BLOG'
    }
    return render(request, 'main/blog.html', context)

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data
            return redirect('login')
    else:
        form = Registration()
        
    return render(request, 'main/register.html', {'form':form, 'title':'REGISTER'})
