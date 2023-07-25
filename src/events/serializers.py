from rest_framework import serializers
from .models import Category, Club, Event, University

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'wilaya', 'number_attendants', 'description', 'event_start_date', 'body', 'category', 'clubs', 'university', 'is_verified']

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'description', 'body', 'university']

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'club_set']