from django.conf.urls import url, include
from django.urls import path
#from sports.api.views import TeamAPIView
from . import views as sports_views
from django.views.generic import TemplateView

from sports.views import SportView, NationView

app_name = 'sports'

urlpatterns = [


    path('<slug:country_slug>/', NationView.as_view(), name='national-home'),
    path('', sports_views.SportView.as_view(), name='sport-home'),
    #url(r'^api_data/', include('sports.api.urls')),
    #url(r'^monthly-view/$', cricket.CricketCalendar.as_view(), name='monthly-view'),
    # path('<slug:country_slug>', sports_views.ListView.as_view(), name='national-home'), #unused
]
