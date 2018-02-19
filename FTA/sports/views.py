from django.shortcuts import render, get_object_or_404
from articles.models import Post
from sports.models import Sport
from django.views.generic.list import ListView

# Create your views here.

class SportView(ListView):
    template_name = "sports/sport-home.html"
    context_object_name = 'sport_list'

    def get_queryset(self):
        self.sport = get_object_or_404(Sport, sport_slug=self.kwargs['sport_slug'])
        return Post.objects.filter(post_category=self.sport)

    def get_context_data(self, **kwargs):
        context = super(SportView, self).get_context_data(**kwargs)
        return context