from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^home', TemplateView.as_view(template_name='bookhome.djhtml'), name='home'),
)
