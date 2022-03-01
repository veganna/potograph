from django.urls import URLPattern, path
from .views import *

app_name = 'StaticPages'

urlpatterns = [
    path('',  index, name='index'),
    path('about/',  about, name='about'),
    path('contact/',  contact, name='contact'),
] 
