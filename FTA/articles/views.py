from django.shortcuts import render, get_object_or_404
from articles.models import Post, VideoNews
from nations.models import Country_Data
from sports.models import Sport
from django.views.generic import ListView, DetailView

# Create your views here.


class IndexView(ListView):
    template_name = "articles/index.html"
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        context = {'all_posts': Post.objects.all()}
        context['video'] = VideoNews.objects.all()
        return context

    def get_queryset(self):
        return Post.objects.all()


class SportNationView(ListView):
    template_name = 'articles/index.html'
    context_object_name = 'all_posts'

    def get_context_data(self, **kwargs):
        context = {'all_posts': Post.objects.all()}
        context['video'] = VideoNews.objects.all()
        return context

    def get_queryset(self):
        self.sport = get_object_or_404(Sport, sport_slug=self.kwargs['sport_slug'])
        self.country = get_object_or_404(Country_Data, country_slug=self.kwargs['country_slug'])
        return Post.objects.filter(post_category=self.sport, country_slug=self.country)


class DetailView(DetailView):
    queryset = Post.objects.all()
    slug_url_kwarg = 'post_slug'
    template_name = 'articles/details.html'
    slug_field = 'post_slug'

    def get_slug_field(self):
        return self.slug_field

    def post_projects(self):
        self.post = get_object_or_404(Post, slug=self.kwargs['post_slug'])
        return Post.objects.filter(post=self.post)
