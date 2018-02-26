from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from articles.models import Post
from sports.models import Sport
from nations.models import Country_Data
from teams.models import Team
from django.views.generic.list import ListView

# Create your views here.


class SportView(ListView):
    template_name = "articles/index.html"
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        context = super(SportView, self).get_context_data(**kwargs)
        context['sport_menu'] = get_object_or_404(Sport, sport_slug=self.kwargs['sport_slug'])
        context['country_selector'] = Country_Data.objects.filter(sport=self.sport).order_by('sport')
        return context

    def get_queryset(self):
        self.sport = get_object_or_404(Sport, sport_slug=self.kwargs['sport_slug'])
        return Post.objects.filter(post_category=self.sport)


class NationView(ListView):
    template_name = "articles/index.html"
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        context = super(NationView, self).get_context_data(**kwargs)
        context['sport_menu'] = get_object_or_404(Sport, sport_slug=self.kwargs['sport_slug'])
        context['country_selector'] = Country_Data.objects.filter(sport=self.sport).order_by('sport')

        return context

    def get_queryset(self):
        self.sport = get_object_or_404(Sport, sport_slug=self.kwargs['sport_slug'])
        self.country = get_object_or_404(Country_Data, country_slug=self.kwargs['country_slug'])
        return Post.objects.filter(post_category=self.sport, country_slug=self.country)

#.distinct('nation',) might work?
# context['country_selector'] = Team.objects.filter(sport=self.sport).values_list('nation', flat=True).distinct() XXdoesnt workXX
