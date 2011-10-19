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
        if parseSubject(subject,'add'):
            pairs = pairBody(body)
            user = getUser(email)
            title = parsePairForKey(pairs,'book')
            friend_loan = parsePairForKey(pairs,'friend')
            book = Book(user=user,title=title,friend_loan=friend_loan)
            book.save()
            sendBook(book,user)
        if parseSubject(subject,'report'):
            sendReport(user)
    except:
        sendError(email)
        


def sendError(email):
    send_mail(
        subject='Error processing request',
        message='Could not do what you wanted me to do',
        from_email=reply_email,
        recipient_list=[email],
        fail_silently=False
        )


def sendReport(user):
    books = user.book_set.all()
    body = '\n'.join([
            ','.join([str(book.date_loan), book.title,book.friend_loan]) for book in books
            ])
    send_mail(
        subject='Loan Report From BookerE',
        message=body,
        from_email=reply_email,
        recipient_list=[user.email],
        fail_silently=False
        )


def sendBook(book,user):
    send_mail(
        subject='Successfully Stored Book!',
        message='Added the following book to your loanouts:\n%s' % ','.join([str(book.date_loan),book.title,book.friend_loan]),
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
        if key in k:
            return pairs[k]
    return False

def parseSubject(subject,key):
    """
    """
    return key in subject
