from django.contrib.gis.geos import Point
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.parsers import FormParser, FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_gis.filters import DistanceToPointFilter
from rest_api.filters import DistanceFilter
from rest_api.models import Spot, Tip, Review, Photo
from rest_api.serializers import SpotSerializer, TipSerializer, ReviewSerializer, PhotoSerializer


class SpotList(ListCreateAPIView):

    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    filter_backends = (DistanceFilter, )
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)


class SpotDetail(RetrieveUpdateDestroyAPIView):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer


class TipDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

class TipList(APIView):

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



class ReviewList(APIView):

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


class PhotoList(APIView):

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