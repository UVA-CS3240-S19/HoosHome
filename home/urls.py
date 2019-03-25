from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
	path('', views.home, name = "homepage"),
	path('createlisting/', views.ListingCreateView.as_view(), name='createlisting'),
    path('listings', views.ListingList.as_view(), name='listings'),
    path('filters', views.ListingListFilter.as_view(), name='filters'),
	path('search', views.search, name='search'),
    path('simplesearch', views.simpleFilter, name='search'),
    path("test",views.testone, name="test")
]
