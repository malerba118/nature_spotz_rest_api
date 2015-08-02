from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api import views

urlpatterns = [
    url(r'^spots/$', views.SpotList.as_view(), name="spot-list"),
    url(r'^spots/(?P<pk>[0-9]+)/$', views.SpotDetail.as_view(), name="spot-detail"),
    url(r'^tips/(?P<pk>[0-9]+)/$', views.TipDetail.as_view(), name="tip-detail"),
    url(r'^spots/(?P<pk>[0-9]+)/tips/$', views.TipList.as_view(), name="tip-list"),
    url(r'^reviews/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view(), name="review-detail"),
    url(r'^spots/(?P<pk>[0-9]+)/reviews/$', views.ReviewList.as_view(), name="review-list"),
    url(r'^photos/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view(), name="photo-detail"),
    url(r'^spots/(?P<pk>[0-9]+)/photos/$', views.PhotoList.as_view(), name="photo-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)