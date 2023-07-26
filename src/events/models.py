from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class University(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    
    universities = models.ManyToManyField(University, related_name='clubs', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=255)
    wilaya = models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(58), MinValueValidator(1)])
    number_attendants = models.PositiveIntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    event_start_date = models.DateTimeField()
    body = models.TextField(null=True, blank=True)

    category = models.ForeignKey(Category,related_name = 'events', on_delete=models.SET_NULL, null=True, blank=True)
    clubs = models.ManyToManyField(Club, related_name = 'events', blank=True)
    universities = models.ManyToManyField(University, related_name = 'events', blank=True)

    slug = models.SlugField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #change to cascade for deployment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name