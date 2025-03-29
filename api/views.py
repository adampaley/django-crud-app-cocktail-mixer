from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cocktail, Ingredient
from .forms import ServingForm

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def cocktail_index(request):
    cocktails = Cocktail.objects.all()
    return render(request, 'cocktails/index.html', {'cocktails': cocktails})

@login_required
def cocktail_detail(request, cocktail_id):
    cocktail = Cocktail.objects.get(id=cocktail_id)
    unused_ingredients = Ingredient.objects.exclude(id__in = cocktail.ingredients.all().values_list('id'))

    serving_form = ServingForm()
    return render(request, 'cocktails/detail.html', {
        'cocktail': cocktail, 'serving_form': serving_form, 'ingredients': unused_ingredients
    })

class CocktailCreate(LoginRequiredMixin, CreateView):
    model = Cocktail
    fields = ['name', 'cost', 'description', 'glassware']

    def form_valid(self, form):
        form.instance.submitted_by = self.request.user
        return super().form_valid(form)
    

class CocktailUpdate(LoginRequiredMixin, UpdateView):
    model = Cocktail
    fields = ['cost', 'description', 'glassware']

class CocktailDelete(LoginRequiredMixin, DeleteView):
    model = Cocktail
    success_url = '/cocktails/'

@login_required
def add_serving(request, cocktail_id):
    form = ServingForm(request.POST)
    if form.is_valid():
        new_serving = form.save(commit=False)
        new_serving.cocktail_id = cocktail_id
        new_serving.save()
    return redirect('cocktail-detail', cocktail_id=cocktail_id)

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient

class IngredientDetail(LoginRequiredMixin, DetailView):
    model = Ingredient

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = '__all__'

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = '/ingredients/'

@login_required
def associate_ingredient(request, cocktail_id, ingredient_id):
    Cocktail.objects.get(id=cocktail_id).ingredients.add(ingredient_id)
    return redirect('cocktail-detail', cocktail_id=cocktail_id)

@login_required
def remove_ingredient(request, cocktail_id, ingredient_id):
    cocktail = Cocktail.objects.get(id=cocktail_id)
    ingredient = Ingredient.objects.get(id=ingredient_id)
    cocktail.ingredients.remove(ingredient)
    return redirect('cocktail-detail', cocktail_id=cocktail.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cocktail-index')
        else: 
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)