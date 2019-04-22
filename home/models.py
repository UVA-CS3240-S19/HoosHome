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
    pub_date = models.DateTimeField('date published', default=timezone.now)
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    features =  models.CharField(max_length=50, default="[]")
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    front_View = models.ImageField(upload_to='front', default='vsabre.jpg')
    interior_View = models.ImageField('Interior View', upload_to='interior', default='vsabre.jpg')
    back_View = models.ImageField('Back View', upload_to='back', default='vsabre.jpg')

    #Use Json to store lists as strings
    def set_features(self, x):
        self.features = json.dumps(x)

    def get_features(self):
        return json.loads(self.features)


    #Review info
    ratings = models.IntegerField(default=0)
    number_of_ratings = models.IntegerField(default=0)
    reviews = models.CharField(max_length=20000, default="[]")
    reviewers = models.CharField(max_length=19000, default="[]")

    # Use Json to store lists as strings
    def set_review(self, x):
        self.reviews = json.dumps(x)

    def get_review(self):
        return json.loads(self.reviews)

    def set_reviewer(self, x):
        self.reviewers = json.dumps(x)

    def get_reviewer(self):
        return json.loads(self.reviewers)

    def get_both(self):
        reviewers = self.get_reviewer()
        reviews = self.get_review()
        temp = []
        for i in range(min(len(reviews),len(reviews))):
            temp.append((reviews[i],reviewers[i]))

        return temp


    #Landlord info
    realtor_agent = models.CharField(max_length=200)
    realtor_site = models.CharField(max_length=200, default="google.com")
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.address)  + " for " + str(self.price) + "\nDescription: " + str(self.description)

    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=50) <= self.pub_date <= now

class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
