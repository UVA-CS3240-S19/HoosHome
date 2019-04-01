from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('createlisting/', views.ListingCreateView.as_view(), name='createlisting'),
    path('listings', views.ListingList.as_view(), name='listings'),
    path('filters', views.ListingListFilter.as_view(), name='filters'),
    path('search', views.search, name='search'),
    path('individual/<int:listing_id>', views.individual, name='individual'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
