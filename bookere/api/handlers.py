from piston.handler import BaseHandler
from books.models import Book

class BookHandler(BaseHandler):
  """book api
  """
  allowed_methods = ('GET','POST',)
  model = Book
    
  def read(self,request):
    """
    
    Arguments:
    - `self`:
    - `request`:
    """
    return request.user.book_set.all()
