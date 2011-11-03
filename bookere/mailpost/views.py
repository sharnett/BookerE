# Create your views here.

from models import MailPost
from django.core.mail import send_mail, EmailMessage

from mailpost.forms import FakeEmailForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.test.client import Client
from django.http import HttpResponseRedirect
from cloudmailin.views import generate_signature

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
    except User.DoesNotExist:
        sendError(email, "Please sign up for BookerE!!!!")
    except Exception as e3:
        sendError(email,e3)

def send_message(email,subject,message):
    from_email = reply_email
    recipient_list = [email]
    fail_silently = False
    headers = {'Reply-To': from_email}
    email = EmailMessage(subject, message, from_email, recipient_list,headers = headers)
    email.send(fail_silently=fail_silently)

def sendError(email,etype):
    subject='Error processing request -- %s' % str(etype)
    message='Could not do what you wanted me to do %s' % str(etype)
    send_message(email,subject,message)

def bookString(book):
    return ','.join([str(book.date_loan),book.title,book.friend_loan])

def booksString(books):
    return '\n'.join([bookString(book) for book in books])

def sendReport(user):
    message = booksString(user.book_set.all())
    subject='Loan Report From BookerE'
    send_message(user.email,subject,message)

def sendBook(book,user):
    subject='Successfully Stored Book!'
    message='Added the following book to your loanouts:\n%s' % bookString(book)
    send_message(user.email,subject,message)
    

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
    return User.objects.get(email=email)

def parsePairForKey(pairs,key):
    for k in pairs.iterkeys():
        if key.lower() in k.lower():
            return pairs[k]
    return False

def parseSubject(subject,key):
    """
    """
    return key.lower() in subject.lower()

def fake_email_view(request):
    form = FakeEmailForm(request.user) 
    return render_to_response('gmail.html', { 'form': form }, context_instance=RequestContext(request) )

def sent_email_view(request):
    form = FakeEmailForm(request.user, request.POST)
    data = request.POST.copy()
    params = dict((k, v) for k, v in request.POST.iteritems())
    data['signature'] = generate_signature(params, request.POST['secret'])
    c = Client()
    c.post('/cloudmailin/', data)
    return HttpResponseRedirect('/books/home')
