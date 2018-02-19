from django.conf.urls import url, include
from django.urls import path
from .views import IndexView, SportView, DetailView
from django.views.generic import TemplateView

app_name = 'articles'

urlpatterns = [
    path('<slug:sport_slug>/<slug:post_slug>', DetailView.as_view(), name='detail'),
    path('', IndexView.as_view(), name='index'),
    
    
    #url(r'^monthly-view/$', cricket.CricketCalendar.as_view(), name='monthly-view'),
    #url(r'^(?P<category_slug>[-_\w]+)/$', sports_views.ListView.as_view(), name='sport-category'),
]
