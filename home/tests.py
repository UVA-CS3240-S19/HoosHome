import unittest
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Users, Listing

class LoginTests(TestCase):
    def testUserTrue(self):
        cavman = Users(username='cavman',password='uva12345')
        self.assertEqual(cavman.username, 'cavman')
    def testUserFalse(self):
        jeff = Users(username='mynamejeff',password='lemonade69')
        self.assertNotEqual(jeff.username, 'mynamenojeff')
    def testPassTrue(self):
        cavman = Users(username='cavman',password='uva12345')
        self.assertEqual(cavman.password, 'uva12345')
    def testPassFalse(self):
        jeff = Users(username='mynamejeff',password='lemonade69')
        self.assertNotEqual(jeff.password, 'lemonade68')
  """      
class ListingInfoTests(TestCase):    
    def testFutureListing(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Listing(pub_date=time)
        self.assertIs(future_question.published_recently(), False)
    def testOldListing(self):
        time = timezone.now() - datetime.timedelta(days=51)
        old_question = Listing(pub_date=time)
        self.assertIs(old_question.published_recently(), False)
    def testRecentListing(self):
        time = timezone.now() - datetime.timedelta(hours=49)
        recent_question = Listing(pub_date=time)
        self.assertIs(recent_question.published_recently(), True)
    def testAddressTrue(self):
        temp = Listing(address="123 Conch Lane")
        self.assertEqual(temp.address, "123 Conch Lane")
    def testAddressFalse(self):
        temp = Listing(address="123 Bonch Bane")
        self.assertNotEqual(temp.address, "123 Conch Lane")
    def testDescTrue(self):
        temp = Listing(description="This place is so cool bro I'd live here")
        self.assertEqual(temp.description, "This place is so cool bro I'd live here")
    def testDescFalse(self):
        temp = Listing(description="This place is so cool bro I'd live here")
        self.assertNotEqual(temp.description, "This place is not so cool bro I'd rather die than live here")
    def testBedsTrue(self):
        temp = Listing(beds=2)
        self.assertEqual(temp.beds, 2)
    def testBedsFalse(self):
        temp = Listing(beds=3)
        self.assertNotEqual(temp.beds, 2)
    def testPriceTrue(self):
        temp = Listing(price=69)
        self.assertEqual(temp.price, 69)
    def testPriceFalse(self):
        temp = Listing(price=420)
        self.assertNotEqual(temp.price, 69)
class ListingReviewTests(TestCase):
    def testRatingsDefault(self):
        temp = Listing()
        self.assertEqual(temp.ratings, 0) 
    def testRatingsTrue(self):
        temp = Listing(ratings=5)
        self.assertEqual(temp.ratings, 5)
    def testRatingsFalse(self):
        temp = Listing(ratings=3)
        self.assertNotEqual(temp.ratings, 5)
    def testNumRatingsDefault(self):
        temp = Listing()
        self.assertEqual(temp.number_of_ratings, 0)
    def testNumRatingsTrue(self):
        temp = Listing(number_of_ratings=20)
        self.assertEqual(temp.number_of_ratings, 20)
    def testNumRatingsFalse(self):
        temp = Listing(number_of_ratings=60)
        self.assertNotEqual(temp.number_of_ratings, 20)
"""
