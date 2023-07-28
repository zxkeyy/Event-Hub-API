from django_filters.rest_framework import FilterSet
from .models import Event, Club, University

class EventFilter(FilterSet):
    class Meta:
        model = Event
        fields = {
            'wilaya': ['exact'],
            'clubs': ['exact'],
            'universities': ['exact'],
            'category': ['exact'],
        }

class ClubFilter(FilterSet):
    class Meta:
        model = Club
        fields = {
            'universities',
        }