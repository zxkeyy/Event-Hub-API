from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Category, Club, Event, University
from .serializers import CategorySerializer, ClubSerializer, EventSerializer, UniversitySerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ClubViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class universityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.request.method in ['GET']:
            self.permission_classes = []
        return super().get_permissions()

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAdminUser]

    # Allow anon to view
    def get_permissions(self):
        if self.request.method in ['GET']:
            self.permission_classes = []
        return super().get_permissions()