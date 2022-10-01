from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')

def blog(request):
    return render(request, 'blog.html')


def pricing(request):
    return render(request, 'pricing.html')
