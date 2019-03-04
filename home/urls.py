from django.urls import path, include
from django.contrib import admin
from home import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('accounts/', include('django.contrib.auth.urls')),
]
