from django.views.generic.list import ListView
from books.models import Book

class bookView(ListView):
    context_object_name = "book_list"
    template_name = "bookhome.djhtml"
    model = Book
    def get_queryset(self):
        return self.request.user.book_set.filter(active=True)

class oldBookView(ListView):
    context_object_name = "book_list"
    template_name = "bookhome.djhtml"
    model = Book
    def get_queryset(self):
        return self.request.user.book_set.filter(active=False)
