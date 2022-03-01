from django.shortcuts import render
from .models import *

# Create your views here.

def categories(request):
    categories = Category.objects.all()
    return render(request, 'Portifolio/services.html', {'categories': categories})

def items(request, category_id):
    items = Items.objects.filter(category_id=category_id) 
    return render(request, 'Portifolio/items.html', {'items': items})
