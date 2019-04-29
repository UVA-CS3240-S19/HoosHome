from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Listing


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Enter a valid email address.')


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=30, required=True)
    BEDS = (("1", "all beds"), ("2", "1 bed"),
            ("3", "2 beds"), ("4", "3 beds"), ("5", "3+ beds"))
    BATHS = (("1", "all baths"), ("2", "1 bath"),
             ("3", "2 baths"), ("4", "3 baths"), ("5", "3+ baths"))
    beds = forms.ChoiceField(choices=BEDS)
    baths = forms.ChoiceField(choices=BATHS)
    days = forms.ChoiceField(choices=[(x, x) for x in range(1, 5)])


class ListingForm(ModelForm):
    gym = forms.BooleanField(required=False)
    parking = forms.BooleanField(required=False)
    wifi = forms.BooleanField(required=False)
    heating = forms.BooleanField(required=False)
    furnished = forms.BooleanField(required=False)
    lounge = forms.BooleanField(required=False)
    laundry = forms.BooleanField(required=False)
    pets = forms.BooleanField(required=False)
    AC = forms.BooleanField(required=False)
    business_center = forms.BooleanField(required=False)

    baths_list = ['1 bath', '2 baths', '3 baths', '4+']

    temp = [(x, x) for x in range(1, 5)]

    baths = forms.ChoiceField(choices=temp)

    beds_list = ['1 bed', '2 beds', '3 beds', '4+']
    beds = forms.ChoiceField(choices=temp)

    class Meta:
        model = Listing
        fields = ('address', 'realtor_agent', 'description', 'front_View',
                  'interior_View', 'back_View', 'price', 'phone_number', 'realtor_site')
