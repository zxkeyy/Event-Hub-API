from rest_framework import serializers
from .models import Category, Club, Event, University

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'location_name', 'location_id', 'wilaya', 'number_attendants', 'description', 'image', 'start_date', 'end_date', 'body', 'category', 'clubs', 'universities', 'slug', 'is_verified']

        read_only_fields = ['is_verified']

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'description', 'image', 'body', 'universities', 'events']

        read_only_fields = ['events']

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'image', 'body', 'clubs' ,'events']

        read_only_fields = ['events', 'clubs']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'events']
        read_only_fields = ['events']