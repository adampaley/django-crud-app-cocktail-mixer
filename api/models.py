from django.db import models
from django.urls import reverse

# Create your models here.
class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    glassware = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cocktail-detail", kwargs={"cocktail_id": self.id})
    