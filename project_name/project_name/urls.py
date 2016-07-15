from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

'''
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap,
}
'''

#If HomeView from pages app is gonna be used, uncomment this and the appropriate url entry
#from apps.pages.views import HomeView

#Enable for SEO
#from djangoseo.admin import register_seo_admin
#from .seo import BasicMetadata
#register_seo_admin(admin.site, BasicMetadata)

urlpatterns = [
    #Enable if grappelli is installed
    #url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', admin.site.urls),
    #url(r'^robots\.txt$', include('robots.urls')),
    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #url(r'^', include('apps.pages.urls')),
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
