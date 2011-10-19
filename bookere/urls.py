from django.conf.urls.defaults import patterns, include, url
from cloudmailin.views import MailHandler
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from mailpost.views import create_post

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('bookere.frontend.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),
                       url(r'register/',include('register.urls',app_name='register',namespace='register'))
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)

mail_handler = MailHandler()
mail_handler.register_address(
    address="39b5ef0e6660524333d3@cloudmailin.net",
    secret= "9e6a1be956c7ef8aea57",    
    callback=create_post,
    )

urlpatterns += patterns('',
                       url(r'^cloudmailin/$', mail_handler),
                       )
