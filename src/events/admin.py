from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'is_verified']
    autocomplete_fields = ['category', 'clubs', 'universities', 'tags', 'owner']
    prepopulated_fields = {
        'slug' : ['name']
    }


@admin.register(models.Club)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']

    autocomplete_fields = ['universities', 'owner']
    search_fields = ['name']

@admin.register(models.University)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name']

    search_fields = ['name']

@admin.register(models.Category)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name']

    search_fields = ['name']

@admin.register(models.Tag)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name']

    search_fields = ['name']