from unicodedata import category
from django.shortcuts import render
from Portfolio.models import *
from .models import *

# Create your views here.

def index(request):
    context = {}
    context["category_list"] = Category.objects.all()
    context["hero_carrousel_list"] = HeroCarrousel.objects.all()
    context["experience_list"] = experience.objects.all()
    return render(request, 'StaticPages/index.html', context)

def about(request):
    return render(request, 'StaticPages/about.html')

def portfolio(request):
    return render(request, 'StaticPages/portfolio.html')

def services(request):
    return render(request, 'StaticPages/services.html')

def contact(request):
    return render(request, 'StaticPages/contact.html')

