from django.db import models
from django.urls import reverse

# Create your models here.

COCKTAIL_COMPONENTS = (
    ('A', 'Alcohol'),
    ('L', 'Liqueur'),
    ('M', 'Mixer'),
    ('G', 'Garnish'),
    ('I', 'Ice'),
    ('F', 'Flavoring')
)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    categorization = models.CharField(
        max_length=1,
        choices=COCKTAIL_COMPONENTS,
        default=COCKTAIL_COMPONENTS[0][0]
    )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ingredient-detail", kwargs={"pk": self.id})
    
    def get_categorization(self):
        categorization_map = dict(COCKTAIL_COMPONENTS)
        return categorization_map.get(self.categorization, "Default")
    
GLASS_TYPES = (
    ('C', 'collins'),
    ('H', 'highball'),
    ('M', 'martini'),
    ('R', 'rocks'),
    ('S', 'shot'),
    ('U', 'coupe'),
    ('W', 'wine'),
)

class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    glassware = models.CharField(
        max_length=1,
        choices=GLASS_TYPES,
        default=GLASS_TYPES[1][0]
    )
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cocktail-detail", kwargs={"cocktail_id": self.id})
    
    def get_glassware_name(self):
        glassware_map = dict(GLASS_TYPES)
        return glassware_map.get(self.glassware, "Default")

SERVING_SIZES = (
    ('S', 'Single'),
    ('D', 'Double')
)    

class Serving(models.Model):
    date = models.DateField('Serving Date')
    jigger = models.CharField(
        max_length=1,
        choices=SERVING_SIZES,
        default=SERVING_SIZES[0][0]
    )

    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_jigger_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']