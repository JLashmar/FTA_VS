from django.db import models
from django.urls import reverse

from nations.models import Country_Data
from sports.models import Sport
from django.db.models.fields import DateTimeField
from embed_video.fields import EmbedVideoField

# Create your models here.


def get_upload_path(instance, filename):
    return "%s/%s/%s" % (instance.post_category.name, instance.team_a.team_name, filename)


class Post(models.Model):
    title = models.CharField(max_length=100, unique=False)
    post_slug = models.SlugField(max_length=100, unique=True)
    post_category = models.ForeignKey(Sport, related_name='post_category', on_delete=models.CASCADE)
    team_a = models.ForeignKey('teams.Team', related_name='first_team', on_delete=models.CASCADE, blank=True, null=True)
    team_b = models.ForeignKey('teams.Team', related_name='second_team', on_delete=models.CASCADE, blank=True, null=True)
    short_description = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField()
    headline_image = models.ImageField(blank=True, null=True, upload_to=get_upload_path)
    headline_image_credit = models.CharField(max_length=150, blank=True, null=True)
    post_image = models.ImageField(blank=True, null=True, upload_to=get_upload_path)
    post_image_credit = models.CharField(max_length=150, blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    country_slug = models.ManyToManyField(Country_Data, related_name='nation_slug')
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'sport_slug': self.post_category.sport_slug, 'post_slug': self.post_slug})


class VideoNews(models.Model):
    title = models.CharField(max_length=100, unique=True)
    related_post = models.ForeignKey('Post', blank=True, null=True, on_delete=models.CASCADE)
    link = models.URLField()
    video = EmbedVideoField()  # same like models.URLField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return self.title
