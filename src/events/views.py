from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Category, Club, Event, University, Tag
from .serializers import CategorySerializer, ClubSerializer, EventSerializer, UniversitySerializer, TagSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import EventFilter, ClubFilter

# Create your views here.
class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    lookup_field = 'slug'
    
    filter_backends =[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EventFilter
    search_fields = ['name', 'description', 'location_name', 'clubs__name', 'universities__name', 'tags__name']
    ordering_fields = ['name', 'start_date', 'end_date', 'created_at', 'updated_at', 'priority']
    

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

    filter_backends =[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ClubFilter
    search_fields = ['name', 'description', 'universities__name', 'events__name']
    ordering_fields = ['name', 'priority']

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
    
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    
    def get_permissions(self):
        if self.request.method in ['GET']:
            self.permission_classes = []
        return super().get_permissions()

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAdminUser]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

    # Allow anon to view
    def get_permissions(self):
        if self.request.method in ['GET']:
            self.permission_classes = []
        return super().get_permissions()
    
class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    permission_classes = [IsAdminUser]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

    # Allow anon to view
    def get_permissions(self):
        if self.request.method in ['GET']:
            self.permission_classes = []
        return super().get_permissions()