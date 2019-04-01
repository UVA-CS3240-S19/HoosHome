from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    #class Meta:
     #   model = User
      #  fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class SearchForm(forms.Form):
    search_text = forms.CharField(max_length = 30, required = True)
    
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ('pub_date', 'address', 'realtor_agent', 'description','front_View','interior_View','back_View', 'price')
