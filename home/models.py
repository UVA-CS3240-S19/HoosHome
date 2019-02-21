import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Listing(models.Model):
    pub_date = models.DateTimeField('date published')
    address = models.CharField(max_length=200)
    realtor_agent = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.address

    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=50) <= self.pub_date <= now

class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)