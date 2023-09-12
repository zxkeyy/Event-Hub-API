from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from .validators import validate_file_size

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='images/categories/', null=True, blank=True)


    def __str__(self) -> str:
        return self.name

class University(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/universities/', null=True, blank=True, validators=[validate_file_size])
    body = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/clubs/', null=True, blank=True, validators=[validate_file_size])
    body = models.TextField(blank=True, null=True)
    
    universities = models.ManyToManyField(University, related_name='clubs', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    priority = models.IntegerField(default=1)


    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=64)
    location_name = models.CharField(max_length=255)
    location_id = models.CharField(max_length=255)
    wilaya = models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(58), MinValueValidator(1)])
    number_attendants = models.PositiveIntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='images/events/', null=True, blank=True, validators=[validate_file_size])
    body = models.TextField(null=True, blank=True)

    category = models.ForeignKey(Category,related_name = 'events', on_delete=models.SET_NULL, null=True, blank=True)
    clubs = models.ManyToManyField(Club, related_name = 'events', blank=True)
    universities = models.ManyToManyField(University, related_name = 'events', blank=True)
    tags = models.ManyToManyField(Tag, related_name='events', blank=True)

    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #change to cascade for deployment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)

    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name