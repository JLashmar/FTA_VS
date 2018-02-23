from django.conf.urls import url
from django.urls import include, path
from .views import AthleteAPIView, AthleteRudView

urlpatterns = [
    path('athlete/', AthleteAPIView.as_view(), name='athlete-create'),
    path('athlete/<int:pk>/', AthleteRudView.as_view(), name='athlete-rud'), 
]
