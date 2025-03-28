from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cocktail

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cocktail_index(request):
    cocktails = Cocktail.objects.all()
    return render(request, 'cocktails/index.html', {'cocktails': cocktails})

def cocktail_detail(request, cocktail_id):
    cocktail = Cocktail.objects.get(id=cocktail_id)
    return render(request, 'cocktails/detail.html', {'cocktail': cocktail})

class CocktailCreate(CreateView):
    model = Cocktail
    fields = '__all__'

class CocktailUpdate(UpdateView):
    model = Cocktail
    fields = ['cost', 'description', 'glassware']

class CocktailDelete(DeleteView):
    model = Cocktail
    success_url = '/cocktails/'