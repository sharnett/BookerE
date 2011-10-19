from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.djhtml'), name='home'),
)
