from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from . models import TermCs, Blog, TermSe, BugReport
from django.contrib.auth.models import User
from django.contrib import messages
from  main.forms import BlogForm, ContactForm

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

def support(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Your bug has been reported succesfully, Thank you!")
            form.cleaned_data
            return redirect('homedatabase')
        else:
            messages.error(request, "Sorry we couldn't recieve your report try again later!")

    else:
        form = ContactForm(instance = request.user)

    return render(request, 'database/studentsupport.html', {'title':'STUDENT SUPPORT', 'form':form})

@user_passes_test(lambda u: u.is_superuser)
def bugreport(request):
    context = {
        'databr':BugReport.objects.all().order_by('-date'),
        'title':'BUG REPORT'
    }
    return render(request, 'database/bugreport.html', context)



