from django.forms.models import ModelForm
from models import Book

class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'friend_loan')
