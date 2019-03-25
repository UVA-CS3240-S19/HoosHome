import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Listing(models.Model):
    pub_date = models.DateTimeField('date published')
    address = models.CharField(max_length=200)
    realtor_agent = models.CharField(max_length=200)
    description = models.TextField()
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    #bedsbaths = models.CharField(max_length=200, default="2B/2B")
    price = models.IntegerField()
    ratings = models.IntegerField(default=0)



    def __str__(self):
        return str(self.address)  + " for " + str(self.price) + "\nDescription: " + str(self.description)

    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=50) <= self.pub_date <= now

class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
