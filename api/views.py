from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello ᗢ</h1>')

def about(request):
    return HttpResponse('<h1>About the Cocktail Mixer</h1>')