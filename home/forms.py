from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Listing

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    #class Meta:
     #   model = User
      #  fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class SearchForm(forms.Form):
    search_text = forms.CharField(max_length = 30, required = True)
    BEDS = (("1","All Beds"),("2","1 Bed"),("3","2 Beds"),("4","3 Beds"),("5","3+ Beds"))
    BATHS = (("1","All Baths"),("2","1 Bath"),("3","2 Baths"),("4","3 Baths"),("5","3+ Baths"))
    beds = forms.ChoiceField(choices=BEDS)
    baths = forms.ChoiceField(choices=BATHS)
    days = forms.ChoiceField(choices=[(x, x) for x in range(1, 5)])

class ListingForm(ModelForm):
    gym = forms.BooleanField(required = False)
    parking = forms.BooleanField(required = False)
    wifi = forms.BooleanField(required = False)
    heating = forms.BooleanField(required = False)
    furnished = forms.BooleanField(required = False)
    lounge = forms.BooleanField(required = False)
    laundry = forms.BooleanField(required = False)
    pets = forms.BooleanField(required = False)
    AC = forms.BooleanField(required = False)
    business_center = forms.BooleanField(required = False)

    baths_list =['1 bath','2 baths', '3 baths', '4+']

    temp1 = [(x,x) for x in range(1,5)]

    baths = forms.ChoiceField(choices=temp1)

    temp2 = [(x,x) for x in range(1,9)]
    beds_list =['1 bed','2 beds', '3 beds', '4+']
    beds = forms.ChoiceField(choices=temp2)

    class Meta:
        model = Listing
        fields = ('address', 'realtor_agent', 'description','front_View','interior_View','back_View', 'price', 'phone_number', 'realtor_site')
