from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=100, unique=True)

class Dog(models.Model):
    dog = models.CharField(max_length=100)

class Event(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events"
    )
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="location"
    )
    participants = models.ManyToManyField('Dog', related_name='event_participants')
    short_description = models.CharField(max_length=200)
    # max_participants = models.IntegerField(null=True, blank=True, default=None)

    # def add_participant(self, dog):
    #     if self.max_participants is None or self.participants.count() < self.max_participants:
    #         self.participants.add(dog)
    #     else:
    #         raise ValueError("Maximum number of participants reached")

    def __str__(self):
        return self.title



