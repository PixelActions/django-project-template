from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()


#If HomeView from pages app is gonna be used, uncomment this and the appropriate url entry
#from apps.pages.views import HomeView

urlpatterns = patterns('',
    #Enable if grappelli is installed
    #url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^pages/', include('apps.pages.urls')),
    #url(r'^$', HomeView.as_view(), name='home'),
)



if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
    

urlpatterns += staticfiles_urlpatterns()

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )