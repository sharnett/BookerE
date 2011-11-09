from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    friend_loan = models.CharField("Friend", max_length=50)
    date_loan = models.DateTimeField(auto_now_add=True,auto_now=True)
    title = models.CharField("Title", max_length=200)
    user = models.ForeignKey(User,blank=False,null=False)
    active = models.BooleanField(default=True)
