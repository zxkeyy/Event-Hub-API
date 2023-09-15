from rest_framework import serializers
from .models import Category, Club, Event, University, Tag

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'location_name', 'location_id', 'wilaya', 'number_attendants', 'description', 'image', 'start_date', 'end_date', 'body', 'tags', 'category', 'clubs', 'universities', 'slug', 'owner', 'is_verified']

        lookup_field = 'slug'
        read_only_fields = ['owner','is_verified']

class EventSlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'slug']

        lookup_field = 'slug'

class ClubSerializer(serializers.ModelSerializer):
    events = EventSlugSerializer(many=True)
    class Meta:
        model = Club
        fields = ['id', 'name', 'description', 'image', 'body', 'universities', 'owner', 'events']

        read_only_fields = ['owner','events']

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

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'events']
        read_only_fields = ['events']