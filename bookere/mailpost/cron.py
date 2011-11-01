from django_cron import cronScheduler, Job
from models import MailPost
from datetime import datetime
# This is a function I wrote to check a feedback email address and add it to our database. Replace with your own imports


class StoreBullshitPost(Job):
  """
  test class to store bull shit
  """
  run_every = 20

  def job(self):
    """
    store a bull shit record
    """
    email = 'bull@shit.com'
    body = 'I am storing bull shit'
    now = str(datetime.now())
    body+=now
    MailPost(body=body,email=email).save()

cronScheduler.register(StoreBullshitPost)
