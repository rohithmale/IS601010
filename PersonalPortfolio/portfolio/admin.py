from django.contrib import admin
from .models import Project 
# Register your models here.

class Projectcol(admin.ModelAdmin):
    list_display = ('title', 'description', 'year')



admin.site.register(Project, Projectcol)