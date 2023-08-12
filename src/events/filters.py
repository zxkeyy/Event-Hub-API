from django_filters.rest_framework import FilterSet, DateFilter
from .models import Event, Club, University

class EventFilter(FilterSet):
    #start_date = DateFilter(field_name='start_date',lookup_expr=('lt'),) 
    #end_date = DateFilter(field_name='end_date',lookup_expr=('gt'))

    class Meta:
        model = Event
        fields = {
            'wilaya': ['exact'],
            'clubs': ['exact'],
            'universities': ['exact'],
            'category': ['exact'],
            'tags': ['exact'],
            'start_date': ['lt', 'gt'],
            'end_date': ['lt', 'gt'],
        }

class ClubFilter(FilterSet):
    class Meta:
        model = Club
        fields = {
            'universities',
        }