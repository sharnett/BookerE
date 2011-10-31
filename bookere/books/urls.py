from django.conf.urls.defaults import patterns, include, url
from books.views import bookView, oldBookView

urlpatterns = patterns('',
    url(r'^home', bookView.as_view(), name='home'),
    url(r'^history', oldBookView.as_view(), name='history'),
)
