#!/bin/sh
python3 manage.py shell
from home.models import Listing
from django.utils import timezone
Listing.objects.all().delete()

A = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
q = Listing(pub_date = timezone.now(), address = "JPA 1819", realtor_agent = "Unknown", description = A, bedsbaths = "1B/1B", price = 500, ratings = 1)
q.save()
q = Listing(pub_date = timezone.now(), address = "The Pavilion at North Grounds", realtor_agent = "Unknown", description = "A, bedsbaths = "2B/2B", price = 700, ratings = 2)
q.save()
q = Listing(pub_date = timezone.now(), address = "Eagles Landing Apartments", realtor_agent = "Unknown", description = A, bedsbaths = "2B/2B", price = 800, ratings = 3)
q.save()
q = Listing(pub_date = timezone.now(), address = "Wertland Square", realtor_agent = "Unknown", description = A, bedsbaths = "2B/3B", price = 500, ratings = 4)
q.save()
q = Listing(pub_date = timezone.now(), address = "Carrollton Ridge Apts", realtor_agent = "Unknown", description = A, bedsbaths = "4B/2B", price = 999, ratings = 5)
q.save()



print("Success")