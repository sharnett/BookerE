# Create your views here.

from models import MailPost
from django.core.mail import send_mail


from books.models import Book
from django.contrib.auth.models import User

reply_email = "39b5ef0e6660524333d3@cloudmailin.net"

def create_post(**message):
    """
    
    Arguments:
    - `**message`:
    """
    body = message['plain']
    email = message['from']
    subject = message['subject']
    MailPost(body=body,email=email).save()

    try:
        user = getUser(email)
        if parseSubject(subject,'add'):
            try:
                pairs = pairBody(body)            
                title = parsePairForKey(pairs,'book')
                friend_loan = parsePairForKey(pairs,'friend')
                book = Book(user=user,title=title,friend_loan=friend_loan)
                book.save()
                sendBook(book,user)
            except Exception as e1:
                sendError(email,e1)
        if parseSubject(subject,'report'):
            try:
                user = getUser(email)
                sendReport(user)
            except Exception as e2:
                sendError(email,e2)
    except Exception as e3:
        sendError(email,e3)
        
def sendError(email,etype):
    send_mail(
        subject='Error processing request -- %s' % str(etype),
        message='Could not do what you wanted me to do %s' % str(etype),
        from_email=reply_email,
        recipient_list=[email],
        fail_silently=False
        )

def bookString(book):
    return ','.join([str(book.date_loan),book.title,book.friend_loan])

def booksString(book):
    return '\n'.join([bookString(book) for book in books])

def sendReport(user):
    books = user.book_set.all()
    send_mail(
        subject='Loan Report From BookerE',
        message=booksString(books),
        from_email=reply_email,
        recipient_list=[user.email],
        fail_silently=False
        )


def sendBook(book,user):
    send_mail(
        subject='Successfully Stored Book!',
        message='Added the following book to your loanouts:\n%s' % bookString(book),
        from_email=reply_email,
        recipient_list=[user.email],
        fail_silently=False
        )
    

def pairBody(body):
    """
    
    Arguments:
    - `body`:
    """
    lines = body.split('\n')
    pairs = dict()
    for line in lines:
        try:
            splits = line.split(':')
            pairs[splits[0]] = splits[1]
        except:
            continue
    return pairs

def getUser(email):
    return User.objects.filter(email=email)[0]

def parsePairForKey(pairs,key):
    for k in pairs.iterkeys():
        if key.lower() in k.lower():
            return pairs[k]
    return False

def parseSubject(subject,key):
    """
    """
    return key.lower() in subject.lower()
