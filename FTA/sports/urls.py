from django.conf.urls import url, include
#from sports.api.views import TeamAPIView
from . import views as sports_views
from django.views.generic import TemplateView

from sports.views import SportView

app_name = 'sports'

urlpatterns = [
    url(r'^$', sports_views.SportView.as_view(), name='sport-home'),
    #url(r'^api_data/', include('sports.api.urls')),
    #url(r'^monthly-view/$', cricket.CricketCalendar.as_view(), name='monthly-view'),
    url(r'^(?P<category_slug>[-_\w]+)/$', sports_views.ListView.as_view(), name='sport-category'),
]
