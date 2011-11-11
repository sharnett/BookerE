from django.conf.urls.defaults import patterns, include, url
from views import BookView, OldBookView, AddBookView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^home', login_required(BookView.as_view()), name='home'),
    url(r'^history', login_required(OldBookView.as_view()), name='history'),
    url(r'^add', login_required(AddBookView.as_view()), name='add'),
)
