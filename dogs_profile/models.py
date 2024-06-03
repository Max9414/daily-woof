from django.db import models

# Create your models here.

class DogProfile(models.Model):
    AGE_CHOICES = [(i, str(i)) for i in range(1, 21)]

    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    age = models.IntegerField(choices=AGE_CHOICES)
    bitten = models.BooleanField
    rough_play = models.BooleanField
    vaccinated = models.BooleanField

