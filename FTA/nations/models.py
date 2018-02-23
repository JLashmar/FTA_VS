from django.db import models
from django.urls import reverse


class Country_Data(models.Model):
    name = models.CharField(max_length=250)
    country_slug = models.CharField(max_length=250)
    flag = models.ImageField(blank=True, null=True)
    sport = models.ManyToManyField('sports.Sport')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Method level import to avoid circular imports
        from sports.models import Sport
        from articles.models import Post
        super(Country_Data, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:national-home', kwargs={'slug': self.sport, 'country_slug': self.country_slug})
