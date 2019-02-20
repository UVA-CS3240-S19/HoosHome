from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.home, name = "homepage"),
	path('createlisting/', views.ListingCreateView.as_view(), name='createlisting'),
    path('listings', views.ListingList.as_view(), name='listings'),
]
