from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    """
    """

    friend_loan = models.CharField(max_length=50)
    date_loan = models.DateTimeField(auto_now_add=True,auto_now=True)
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User,blank=False,null=False)


        
