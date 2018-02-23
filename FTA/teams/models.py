from django.db import models
from nations.models import Country_Data
from sports.models import Sport

# Create your models here.


class Team(models.Model):
  sport = models.ForeignKey('sports.Sport', on_delete=models.CASCADE)
  #country = CountryField()
  nation = models.ForeignKey(Country_Data, on_delete=models.CASCADE, default='')
  team_name = models.CharField(max_length=250)
  MEN = 'Men'
  WOMEN = 'Women'
  MIXED = 'Mixed'
  GENDER_CHOICES = (
      (MEN, 'Men'),
      (WOMEN, 'Women'),
      (MIXED, 'Mixed'),
  )
  gender = models.CharField(
      max_length=5,
      choices=GENDER_CHOICES,
      default=MEN,
  )
  INTERNATIONAL = 'International'
  DOMESTIC = 'Domestic'
  TIER_CHOICES = (
      (INTERNATIONAL, 'International'),
      (DOMESTIC, 'Domestic')
  )
  tier = models.CharField(
      max_length=13,
      choices=TIER_CHOICES,
      default=MEN,
  )

  def __str__(self):
    return "%s: %s - %s" % (self.sport, self.team_name, self.gender)

  def get_absolute_url(self):
    return reverse('articles:country', kwargs={'country_slug': self.country})
