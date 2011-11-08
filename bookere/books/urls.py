from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from books.models import Book
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    url(r'^home', login_required(TemplateView.as_view(template_name='bookhome.djhtml')), name='home'),
    url(r'^add', login_required(CreateView.as_view(template_name='addbook.djhtml', model=Book, success_url='home')), name='add'),
)
