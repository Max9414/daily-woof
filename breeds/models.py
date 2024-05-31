from django.db import models

# Create your models here.

class Keyword(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Breeds(models.Model):
    breed = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    keywords = models.ManyToManyField(Keyword, related_name='keyword')
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.breed
