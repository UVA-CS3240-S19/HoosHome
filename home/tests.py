import datetime
<<<<<<< HEAD

from django.test import TestCase
from .models import Listing

from django.utils import timezone
class ListingTestClass(TestCase):
    def testOldListing(self):
        time = timezone.now() - datetime.timedelta(days=50, seconds=1)
        old_question = Listing(pub_date=time)
        self.assertIs(old_question.published_recently(), False)

    def testNewListing(self):
        time = timezone.now() - datetime.timedelta(days=49)
        recent_question = Listing(pub_date=time)
        self.assertIs(recent_question.published_recently(), True)
=======
import unittest

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Users, Listing

class LoginTest(TestCase):
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
        
class ListingTest(TestCase):
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
    def testSetAddress(self):
        temp = Listing(address="123 Conch Lane")
        self.assertEqual(temp.address, "123 Conch Lane")
    def testAddressString(self):
        temp = Listing(address="Banana Street")
        self.assertEqual(temp.__str__(), "Banana Street")






>>>>>>> master
