from dajaxice.decorators import dajaxice_register
from django.core import serializers
from dajax.core.Dajax import Dajax

@dajaxice_register
def user_books(request):
  dajax = Dajax()
  dajax.alert('the first book title is %s' % request.user.book_set.all()[0].title)
  return dajax.json()
