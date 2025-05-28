from django.shortcuts import render
from .serializers import ClothingSerializer
from rest_framework import generics
from clothing.models import ClothingModel
# Create your views here.
class ClothingListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClothingModel.objects.all()
    serializer_class = ClothingSerializer


class ClothingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothingModel.objects.all()
    serializer_class = ClothingSerializer