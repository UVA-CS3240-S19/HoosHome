import datetime

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
