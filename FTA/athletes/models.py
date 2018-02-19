from django.db import models
from sports.models import Sport
from nations.models import Country_Data

# Create your models here.

class Athlete(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    initials = models.CharField(max_length=10)
    nationality = models.ForeignKey(Country_Data, on_delete=models.CASCADE, default='')
    sport = models.ManyToManyField(Sport)