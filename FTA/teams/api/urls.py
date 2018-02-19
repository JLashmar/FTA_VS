from django.conf.urls import url
from django.urls import include, path
from .views import TeamAPIView, TeamRudView

urlpatterns = [
    path('team/', TeamAPIView.as_view(), name='team-create'),
    path('team/<int:pk>/', TeamRudView.as_view(), name='team-rud'), 
]
