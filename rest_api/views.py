from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    RetrieveAPIView, CreateAPIView
from rest_framework.parsers import FormParser, FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_gis.filters import DistanceToPointFilter
from rest_api.filters import DistanceFilter
from rest_api.models import Spot, Tip, Review, Photo, Favorite, ParkingLocation
from rest_api.permissions import IsOwner
from rest_api.serializers import SpotSerializer, TipSerializer, ReviewSerializer, PhotoSerializer, UserSerializer, \
    FavoriteSerializer, ParkingLocationSerializer


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class SpotList(ListCreateAPIView):

    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    filter_backends = (DistanceFilter, )
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_serializer(self, instance=None, data=None, files=None, many=False, partial=False):
    #     fields = None
    #     if self.request.method == 'GET':
    #         query_fields = self.request.QUERY_PARAMS.get("fields", None)
    #
    #         if query_fields:
    #             fields = tuple(query_fields.split(','))
    #
    #     return SpotSerializer(instance=instance, data=data, many=many, partial=partial, fields=fields)



class SpotDetail(RetrieveUpdateDestroyAPIView):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TipDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TipList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        spot = get_object_or_404(Spot, pk=pk)
        tips = spot.tips
        serializer = TipSerializer(tips, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        spot = get_object_or_404(Spot, pk=pk)
        serializer = TipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(spot=spot, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class ReviewList(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        spot = get_object_or_404(Spot, pk=pk)
        reviews = spot.reviews
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        spot = get_object_or_404(Spot, pk=pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(spot=spot, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PhotoDetail(RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PhotoList(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        spot = get_object_or_404(Spot, pk=pk)
        photos = spot.additional_photos
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        spot = get_object_or_404(Spot, pk=pk)
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(spot=spot)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFavoriteList(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        favorites = Favorite.objects.filter(user=user)
        serializer = FavoriteSerializer(favorites, context={'request': request}, fields=("id", "spot", "created_at",), many=True)
        return Response(serializer.data)


class SpotFavoriteList(APIView):

    def get(self, request, pk):
        spot = get_object_or_404(Spot, pk=pk)
        favorites = Favorite.objects.filter(spot=spot)
        serializer = FavoriteSerializer(favorites, fields=("id", "user",), many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        spot = get_object_or_404(Spot, pk=pk)
        user = request.user
        try:
            favorite = Favorite.objects.get(spot=spot, user=user)
            return Response(status=status.HTTP_302_FOUND)
        except:
            f = Favorite(user=user, spot=spot)
            f.save()
            serializer = FavoriteSerializer(f, fields=("user",))
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def delete(self,  request, pk):
    #     spot = get_object_or_404(Spot, pk=pk)
    #     user = request.user
    #     try:
    #         favorite = Favorite.objects.get(spot=spot, user=user)
    #         favorite.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)


class FavoriteDetail(RetrieveDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwner)


class ParkingLocationDetail(RetrieveUpdateDestroyAPIView):
    queryset = ParkingLocation.objects.all()
    serializer_class = ParkingLocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ParkingLocationList(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        spot = get_object_or_404(Spot, pk=pk)
        parking_locations = spot.parking_locations
        serializer = ParkingLocationSerializer(parking_locations, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        spot = get_object_or_404(Spot, pk=pk)
        serializer = ParkingLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(spot=spot)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSpotList(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        spots = user.spots
        serializer = SpotSerializer(spots, many=True)
        return Response(serializer.data)

class UserReviewList(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        reviews = user.reviews
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)