from django.contrib import admin
from .models import Athlete

# Register your models here.

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'nationality')