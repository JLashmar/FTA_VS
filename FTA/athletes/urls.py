from django.conf.urls import url, include
from django.urls import path
from sports.views import ListView

app_name = 'articles'

urlpatterns = [
    path('api_data', include('athletes.api.urls')),
]

