from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'frontend.views.home', name='home'),
    # url(r'^snowflake/', include('snowflake.foo.urls')),
)
