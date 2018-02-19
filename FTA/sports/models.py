from django.db import models

# Create your models here.

class Sport_Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category_slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
       return  self.name

   #def get_absolute_url(self):
       #return reverse('sports:sport-category', kwargs={'slug':self.category_slug})

class Sport(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    sport_slug = models.SlugField(max_length=100, db_index=True)
    category = models.ForeignKey('Sport_Category', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sports:sport-home', kwargs={'slug':self.sport_slug})