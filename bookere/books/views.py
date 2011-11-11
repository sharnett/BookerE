from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from models import Book
from forms import AddBookForm

class BookView(ListView):
    context_object_name = "book_list"
    template_name = "bookhome.djhtml"
    model = Book
    def get_queryset(self):
        return self.request.user.book_set.filter(active=True)

class OldBookView(ListView):
    context_object_name = "book_list"
    template_name = "bookhome.djhtml"
    model = Book
    def get_queryset(self):
        return self.request.user.book_set.filter(active=False)

class AddBookView(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = "addbook.djhtml"
    success_url = "home"
    def get_form(self, form_class):
        form = super(AddBookView, self).get_form(form_class)
        form.instance.user = self.request.user
        return form
