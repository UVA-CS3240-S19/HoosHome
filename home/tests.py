from django.test import TestCase

import datetime
import unittest

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Users, Listing
class LoginTest(TestCase):
    def testUserPass(self):
        cavman = Users(username='cavman',password='uva12345')
        self.assertEqual(cavman.username, 'cavman')
class ListingTest(TestCase):
    def testFutureListing(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Listing(pub_date=time)
        self.assertIs(future_question.published_recently(), False)

    def testOldQuestion(self):
        time = timezone.now() - datetime.timedelta(days=51)
        old_question = Listing(pub_date=time)
        self.assertIs(old_question.published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=49)
        recent_question = Listing(pub_date=time)
        self.assertIs(recent_question.published_recently(), True)






