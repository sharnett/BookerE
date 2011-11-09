from django.conf.urls.defaults import patterns, include, url
from books.views import bookView, oldBookView
from django.views.generic.edit import CreateView
from books.models import Book
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^home', login_required(bookView.as_view()), name='home'),
    url(r'^history', login_required(oldBookView.as_view()), name='history'),
    url(r'^add', login_required(CreateView.as_view(template_name='addbook.djhtml', model=Book, success_url='home')), name='add'),
)
