
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from myapp.views import app

urlpatterns = [
    path('admin/', admin.site.urls),
]
