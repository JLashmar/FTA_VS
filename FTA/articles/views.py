from django.shortcuts import render, get_object_or_404
from articles.models import Post, VideoNews
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

class SportView(ListView):
    queryset = Post.objects.all()
    slug_url_kwarg = 'sport_slug'
    template_name = 'articles/index.html'
    slug_field = 'sport_slug'

    def get_slug_field(self):
        return self.slug_field

    def post_projects(self):
        self.post = get_object_or_404(Post, slug=self.kwargs['post_category'])
        return Post.objects.filter(post=self.post)

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