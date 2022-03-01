from django.urls import path
from .views import *
from .models import *

app_name = 'Portifolio'

urlpatterns = [
    path('',  categories, name='categories'),
    path('<int:category_id>/',  items, name='items'),
]
