from django.contrib import admin
from django.urls import path
import crawler.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crawler.views.home, name="home"),
]
