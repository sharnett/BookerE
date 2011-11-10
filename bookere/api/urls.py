from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import BookHandler
from piston.doc import documentation_view
book_handler = Resource(BookHandler)

urlpatterns = patterns('',
                       url(r'^books/', book_handler),
                       # automated documentation
                       url(r'^$', documentation_view),
)
