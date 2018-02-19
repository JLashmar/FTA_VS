from django.contrib import admin
from .models import Sport_Category, Sport

@admin.register(Sport_Category)
class SportCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_slug')
    prepopulated_fields = {'category_slug': ('name',)}


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'sport_slug': ('name',)}