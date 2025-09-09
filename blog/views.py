# blog/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about_me(request):
    return render(request, 'about_me.html')

def blog_list(request):
    return render(request, 'blog_list.html')