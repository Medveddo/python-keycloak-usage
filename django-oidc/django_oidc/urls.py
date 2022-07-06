from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path('', view=home),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('admin/', admin.site.urls),
]
