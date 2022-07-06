from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path

def home(request: HttpRequest):
    return HttpResponse("Home page")

urlpatterns = [
    path('', view=home),
    path('admin/', admin.site.urls),
]
