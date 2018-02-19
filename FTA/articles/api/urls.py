from django.conf.urls import url
from django.urls import include, path
from .views import PostAPIView, PostRudView

urlpatterns = [
    path('post/', PostAPIView.as_view(), name='post-article-create'),
    path('post/<int:pk>/', PostRudView.as_view(), name='post-article-rud'), 
]
