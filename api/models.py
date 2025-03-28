from django.db import models

# Create your models here.
class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    glassware = models.CharField(max_length=50)

    def __str__(self):
        return self.name