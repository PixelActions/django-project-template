from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^(?P<page_template_name>[\w-]+)/$', views.TemplateLocatorView.as_view(), name='template_locator'),
    #url(r'^subsection/(?P<page_template_name>[\w-]+)/$', views.TemplateLocatorView.as_view(subfolder='subsection'), name='template_locator_subsection'),
    #url(r'^contact/$', views.ContactView.as_view(), name='pages_contact'),
)
