from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Cocktail:
    def __init__(self, name, cost, description, glassware):
        self.name = name
        self.cost = cost
        self.description = description
        self.glassware = glassware

# Martini,  Rocks, Coupe, Collins, Wine
# Highball, Shot

cocktails = [
    Cocktail("Margarita", 12, "A refreshing and tangy drink that's perfect for any occasion, especially on a warm day.", "coupe"),
    Cocktail("Old Fashioned", 14, "Served over ice, the Old Fashioned offers a smooth and slightly sweet flavor, with a touch of aromatic complexity.", "rocks"),
    Cocktail("Mojito", 10, "A crisp and refreshing drink. The combination of mint and lime makes it a popular choice for hot weather.", "highball"),
    Cocktail("Negroni", 13, "An Italian classic, this cocktail is known for its bittersweet flavor and is perfect for those who appreciate bold, complex drinks.", "rocks")    
]

def cocktail_index(request):
    return render(request, 'cocktails/index.html', {'cocktails': cocktails})