import datetime
import json
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

class Listing(models.Model):

    #city = models.CharField(max_length=50,default="Charlottesville")
    #zip = models.CharField("ZIP / Postal code", max_length=12,default=22903)
    #bedsbaths = models.CharField(max_length=200, default="2B/2B")

    #Listing info
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    features =  models.CharField(max_length=50, default="[]")
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    front_View = models.ImageField(upload_to='media', default='static/images/rotunda')
    interior_View = models.ImageField('Interior View', upload_to='individual', default='static/images/rotunda')
    back_View = models.ImageField('Back View', upload_to='media', default='static/images/rotunda')

    #Use Json to store lists as strings
    def set_features(self, x):
        self.features = json.dumps(x)

    def get_features(self):
        return json.loads(self.features)


    #Review info
    ratings = models.IntegerField(default=0)
    number_of_ratings = models.IntegerField(default=0)
    reviews = models.CharField(max_length=20000, default="[]")

    # Use Json to store lists as strings
    def add_review(self, x):
        self.set_review(self.get_review().append(x))

    def set_review(self, x):
        self.reviews = json.dumps(x)

    def get_review(self):
        return json.loads(self.reviews)


    #Landlord info
    realtor_agent = models.CharField(max_length=200)
    realtor_site = models.CharField(max_length=200, default="google.com")
    phone_number = models.CharField(max_length=15, default="999-999-9999")

    def __str__(self):
        return str(self.address)  + " for " + str(self.price) + "\nDescription: " + str(self.description)

    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=50) <= self.pub_date <= now

class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
