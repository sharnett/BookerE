# Create your views here.

from models import MailPost
from django.core.mail import send_mail


def create_post(**message):
    """
    
    Arguments:
    - `**message`:
    """
    body = message['plain']
    email = message['from']
    MailPost(body=body,email=email).save()

    send_mail('Received Message','You sent: %s' % body,'noreply@example.com', [email],fail_silently=True)
