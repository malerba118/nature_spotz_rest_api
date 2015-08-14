from django.conf.urls import url, include
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
    url(r'^parking-locations/(?P<pk>[0-9]+)/$', views.ParkingLocationDetail.as_view(), name="parking-location-detail"),
    url(r'^spots/(?P<pk>[0-9]+)/parking-locations/$', views.ParkingLocationList.as_view(), name="parking-location-list"),
    url(r'^users/$', views.UserList.as_view(), name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="user-detail"),
    url(r'^users/(?P<pk>[0-9]+)/reviews/$', views.UserReviewList.as_view(), name="user-review-list"),
    url(r'^users/(?P<pk>[0-9]+)/spots/$', views.UserSpotList.as_view(), name="user-spot-list"),
    url(r'^users/(?P<pk>[0-9]+)/favorites/$', views.UserFavoriteList.as_view(), name="user-favorite-list"),
    url(r'^spots/(?P<pk>[0-9]+)/favorites/$', views.SpotFavoriteList.as_view(), name="spot-favorite-list"),
    url(r'^favorites/(?P<pk>[0-9]+)/$', views.FavoriteDetail.as_view(), name="favorite-detail"),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)