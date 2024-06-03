from django.db import models

# Create your models here.

class Breed(models.Model):
    breed = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField()

    def __str__(self):
        return self.breed
