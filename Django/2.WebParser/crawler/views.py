from django.shortcuts import render
import crawler.crawler

# Create your views here.

def home(request):
    dict = crawler.crawler.getTemp()
    return render(request, "home.html",{"dict":dict})