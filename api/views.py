from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cocktail, Ingredient
from .forms import ServingForm

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
    serving_form = ServingForm()
    return render(request, 'cocktails/detail.html', {
        'cocktail': cocktail, 'serving_form': serving_form
    })

class CocktailCreate(CreateView):
    model = Cocktail
    fields = '__all__'

class CocktailUpdate(UpdateView):
    model = Cocktail
    fields = ['cost', 'description', 'glassware']

class CocktailDelete(DeleteView):
    model = Cocktail
    success_url = '/cocktails/'

def add_serving(request, cocktail_id):
    form = ServingForm(request.POST)
    if form.is_valid():
        new_serving = form.save(commit=False)
        new_serving.cocktail_id = cocktail_id
        new_serving.save()
    return redirect('cocktail-detail', cocktail_id=cocktail_id)

class IngredientCreate(CreateView):
    model = Ingredient
    fields = '__all__'

class IngredientList(ListView):
    model = Ingredient

class IngredientDetail(DetailView):
    model = Ingredient

class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = '__all__'

class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = '/ingredients/'