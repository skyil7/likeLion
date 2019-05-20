from django.shortcuts import render
from .models import article

def home(request):
    articles = article.objects
    return render(request, 'home.html', {'articles':articles})
