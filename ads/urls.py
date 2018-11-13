from django.urls import path

from ads.api import AdListAPIView, AdDetailAPIView
from ads.views import HomeView, AdDetailView, NewAdView

urlpatterns = [
    path('ads/<int:pk>', AdDetailView.as_view(), name='ad_detail'),
    path('ads/new', NewAdView.as_view(), name='new_ad'),
    path('', HomeView.as_view(), name='home'),

    # API
    path('api/1.0/ads/', AdListAPIView.as_view(), name='ad_list_api'),
    path('api/1.0/ads/<int:pk>', AdDetailAPIView.as_view(), name='ad_detail_api')
]
