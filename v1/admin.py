from django.contrib import admin
from django.db.models.aggregates import Count
from .models import Country , City
# Register your models here.
admin.site.register(Country)
admin.site.register(City)
