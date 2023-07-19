from django.db import models

# Create your models here.
class User(models.Model): # place holder
    username = models.CharField(max_length=32)

class Category(models.Model):
    title = models.CharField(max_length=32)

class University(models.Model):
    name = models.CharField(max_length=64)

class Club(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    body = models.TextField()
    
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)


class Event(models.Model):
    title = models.CharField(max_length=64)
    location = models.CharField(max_length=255)
    wilaya = models.PositiveIntegerField(null=True)
    number_attendants = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=255, blank=True)
    event_start_date = models.DateTimeField()
    body = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    clubs = models.ManyToManyField(Club, related_name="events")
    university = models.ManyToManyField(University, related_name="universities")

    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.PROTECT) #change to cascade for deployment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

