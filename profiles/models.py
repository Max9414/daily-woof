from django.db import models

# Create your models here.

class Breed(models.Model):
    breed = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return(self.breed)


class DogProfile(models.Model):
    AGE_CHOICES = [(i, str(i)) for i in range(1, 21)]

    name = models.CharField(max_length=200)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    age = models.IntegerField(choices=AGE_CHOICES)
    bitten = models.BooleanField(default=False)
    rough_play = models.BooleanField(default=False)
    vaccinated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


class HumanProfile(models.Model):
    name = models.CharField(max_length=200)
    dogs = models.ManyToManyField(DogProfile)