from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
import django.contrib.auth.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('articles.urls')),
    path('<sport_slug>/', include('sports.urls')),

    #apis
    path('api/', include('articles.api.urls')),
    path('api/', include('teams.api.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    #path(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)