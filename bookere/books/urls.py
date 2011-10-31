from django.conf.urls.defaults import patterns, include, url
from books.views import bookView

urlpatterns = patterns('',
    url(r'^home', bookView.as_view(), name='home'),
)
