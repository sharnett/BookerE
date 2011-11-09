from django.conf.urls.defaults import patterns, include, url
from cloudmailin.views import MailHandler
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from mailpost.views import create_post, fake_email_view
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                       url(r'^books/', include('books.urls',namespace='books',app_name='books')),                       
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^accounts/', include('registration_backend.urls',namespace="registration",app_name="registration")),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
                        url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
                            url(r'^', include('bookere.frontend.urls',namespace='frontend',app_name='frontend')),
)

mail_handler = MailHandler()
my_address="39b5ef0e6660524333d3@cloudmailin.net"
my_secret= "9e6a1be956c7ef8aea57"
mail_handler.register_address(
    address = my_address,
    secret = my_secret,
    callback = create_post,
    )

urlpatterns += patterns('',
                       url(r'^cloudmailin/$', mail_handler, name='cloudmailin'),
                       )

urlpatterns += patterns('', 
        url(r'^fake_email_client/$', login_required(fake_email_view.as_view(address=my_address, secret=my_secret))),
        )
