from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import timedelta

class MailPost(models.Model):
    """
    test model for storing mail coming in
    """

    body = models.CharField(max_length=5000,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
        
class MailProfile(models.Model):
    next_reminder = models.DateTimeField(auto_now_add=True)
    reminder_frequency = models.PositiveIntegerField(default=14, validators=[MinValueValidator(1)]) # days
    user = models.OneToOneField(User,blank=False,null=False)
    def refresh_next_reminder(self):
        self.next_reminder += timedelta(self.reminder_frequency)
