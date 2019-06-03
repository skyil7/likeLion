from django.shortcuts import render,get_object_or_404
from .models import article

def home(request):
    articles = article.objects
    return render(request, 'home.html', {'articles':articles})

def detail(request, arti_id):
    arti_detail = get_object_or_404(article, pk =arti_id)
    return render(request,'detail.html',{'arti':arti_detail})