from django.contrib import admin
from .models import *
from django.contrib.auth.models import *


admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Items)
