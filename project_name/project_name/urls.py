"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings


#If HomeView from pages app is gonna be used, uncomment this and the appropriate url entry
#from apps.pages.views import HomeView

urlpatterns = [
    #Enable if grappelli is installed
    #url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^pages/', include('apps.pages.urls')),
    #url(r'^$', HomeView.as_view(), name='home'),
]



if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    ]
    

urlpatterns += staticfiles_urlpatterns()

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]
    ]