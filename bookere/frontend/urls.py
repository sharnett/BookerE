from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^help$', TemplateView.as_view(template_name='help.djhtml'), name='help'),
    url(r'^$', TemplateView.as_view(template_name='home.djhtml'), name='home'),
)
