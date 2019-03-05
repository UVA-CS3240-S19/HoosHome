from django.urls import path, include
<<<<<<< HEAD

from . import views

urlpatterns = [
	path('', views.home, name = "homepage"),
	path('createlisting/', views.ListingCreateView.as_view(), name='createlisting'),
    path('listings', views.ListingList.as_view(), name='listings'),
	path('search', views.search, name='search'),
=======
from django.contrib import admin
from home import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
>>>>>>> master
]
