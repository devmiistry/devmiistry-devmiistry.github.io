from django.shortcuts import render

# Create your views here.

def home (request):
    return render (request, 'base/home.html')

def aboutme (request):
    return render(request, 'base/aboutme.html')

def contactme (request):
    return render(request, 'base/contactme.html')


def portfolio (request):
    return render(request, 'base/portfolio.html')


def projects (request):
    return render(request, 'base/projects.html')