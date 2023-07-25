from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Category, Club, Event, University
from .serializers import CategorySerializer, ClubSerializer, EventSerializer, UniversitySerializer

# Create your views here.
class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ClubViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class universityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer