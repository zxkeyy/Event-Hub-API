from rest_framework import serializers
from .models import Category, Club, Event, University

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'wilaya', 'number_attendants', 'description', 'event_start_date', 'body', 'category', 'clubs', 'universities', 'is_verified']

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'description', 'body', 'universities', 'events']

        read_only_fields = ['events']

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'clubs' ,'events']

        read_only_fields = ['events', 'clubs']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'events']
        read_only_fields = ['events']