from django.db import models

# Create your models here.

class PetCare(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(max_length=400)

    def __str__(self):
        return self.title