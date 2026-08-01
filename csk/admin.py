# admin.py in app folder
from django.contrib import admin
from .models import players
# Register your models here.
admin.site.register(players)