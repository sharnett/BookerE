from django_cron import cronScheduler, Job
from models import MailPost, MailProfile
from datetime import datetime
from django.contrib.auth.models import User
from views import sendReport

class SendReminders(Job):
    run_every = 600

    def job(self):
        need_updates = MailProfile.objects.filter(next_reminder__lt=datetime.now())
        for mailprofile in need_updates:
            sendReport(mailprofile.user)
            mailprofile.refresh_next_reminder()

cronScheduler.register(SendReminders)
