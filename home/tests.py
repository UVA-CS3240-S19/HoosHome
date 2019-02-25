from django.test import TestCase

import datetime
import unittest

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Users

class LoginTest(TestCase):
    def setUp(self):
         return Users.objects.create(username='cavman', password='uva123')

    def test_animals_can_speak(self):
        """User can be created"""
        cavman = Users.objects.get(username='cavman')
        self.assertEqual(cavman.username, 'cavman')






