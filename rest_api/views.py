from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.exceptions import ValidationError
from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    RetrieveAPIView
from rest_framework.parsers import FormParser, FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_api.filters import DistanceFilter, SpotFilter, UserFavoriteFilter, UserReviewFilter
from rest_api.models import Spot, Tip, Review, Photo, Favorite, ParkingLocation
from rest_api.permissions import IsOwner, IsOwnerOrReadOnly
from rest_api.serializers import SpotSerializer, TipSerializer, ReviewSerializer, PhotoSerializer, UserSerializer, \
    FavoriteSerializer, ParkingLocationSerializer


class DynamicFieldsViewMixin(object):

     def get_serializer(self, *args, **kwargs):

        serializer_class = self.get_serializer_class()

        fields = None
        if self.request.method == 'GET':
            query_fields = self.request.QUERY_PARAMS.get("fields", None)

            if query_fields:
                fields = tuple(query_fields.split(','))


        kwargs['context'] = self.get_serializer_context()
        kwargs['fields'] = fields

        return serializer_class(*args, **kwargs)



class UserList(DynamicFieldsViewMixin, ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetail(DynamicFieldsViewMixin, RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class SpotList(DynamicFieldsViewMixin, ListCreateAPIView):
    """
    List of spots
    """
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    filter_backends = (DistanceFilter, DjangoFilterBackend)
    filter_class = SpotFilter
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class SpotDetail(DynamicFieldsViewMixin, RetrieveUpdateDestroyAPIView):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class TipDetail(DynamicFieldsViewMixin, RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    permission_classes = (IsOwnerOrReadOnly,)



class TipList(DynamicFieldsViewMixin, ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TipSerializer

    def get_queryset(self):
        spot = get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        return Tip.objects.filter(spot=spot)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            spot=get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        )




class ReviewDetail(DynamicFieldsViewMixin, RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)




class ReviewList(DynamicFieldsViewMixin, ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        spot = get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        return Review.objects.filter(spot=spot)


    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            spot=get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        )




class PhotoDetail(DynamicFieldsViewMixin, RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class PhotoList(DynamicFieldsViewMixin, ListCreateAPIView):

    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        spot = get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        return Photo.objects.filter(spot=spot)

    def perform_create(self, serializer):
        serializer.save(
            spot=get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        )




class UserFavoriteList(DynamicFieldsViewMixin, ListAPIView):

    serializer_class = FavoriteSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserFavoriteFilter

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get("pk", None))
        return Favorite.objects.filter(user=user)



class SpotFavoriteList(DynamicFieldsViewMixin, ListCreateAPIView):

    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        spot = get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        return Favorite.objects.filter(spot=spot)


    def perform_create(self, serializer):
        spot = get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        user = self.request.user
        favorites = Favorite.objects.filter(spot=spot, user=user)
        if favorites.exists():
            raise ValidationError("You have already favorited this spot.")
        serializer.save(user=user, spot=spot)



class FavoriteDetail(DynamicFieldsViewMixin, RetrieveDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsOwnerOrReadOnly,)



class ParkingLocationDetail(DynamicFieldsViewMixin, RetrieveUpdateDestroyAPIView):
    queryset = ParkingLocation.objects.all()
    serializer_class = ParkingLocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class ParkingLocationList(DynamicFieldsViewMixin, ListCreateAPIView):

    serializer_class = ParkingLocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        spot = get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        return ParkingLocation.objects.filter(spot=spot)


    def perform_create(self, serializer):
        spot = get_object_or_404(Spot, pk=self.kwargs.get("pk", None))
        serializer.save(spot=spot)




class UserSpotList(DynamicFieldsViewMixin, ListAPIView):

    serializer_class = SpotSerializer

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get("pk", None))
        return Spot.objects.filter(user=user)



class UserReviewList(DynamicFieldsViewMixin, ListAPIView):

    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = UserReviewFilter

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get("pk", None))
        return Review.objects.filter(author=user)