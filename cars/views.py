from django.shortcuts import render
from rest_framework import generics
from .serialzers import CarSerialzer
from .models import Car
from .permissions import IsAuthenticatedOrReadOnly

class Carlist(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerialzer
    permission_class = (IsAuthenticatedOrReadOnly,)

class CarCreate(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerialzer
    permission_class = (IsAuthenticatedOrReadOnly,)


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerialzer
    permission_class = (IsAuthenticatedOrReadOnly,)