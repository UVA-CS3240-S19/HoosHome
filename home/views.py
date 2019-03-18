from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, ListView
from .forms import SignUpForm, SearchForm
from .models import Listing

class ListingCreateView(CreateView):
    model = Listing
    fields = ('pub_date', 'address', 'realtor_agent', 'description', 'price')

class ListingList(ListView):
    template_name = 'home/index.html'
    context_object_name = 'all_listings'

    def get_queryset(self):
        """Returns recently published listings."""
        return Listing.objects.all()

class ListingListFilter(ListView):
    template_name = 'home/listing_filter.html'
    context_object_name = 'all_listings'

    def get_queryset(self):
        """Returns recently published listings."""
        return Listing.objects.all()

def test(request):
    return render(request, "home/listing_filter_test.html",{})

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            try:
                status = Listing.objects.filter(address__icontains = form.cleaned_data.get("search_text")) # filter returns a list so you might consider skip except part
            except:
                return render(request, "home/search_results.html", {'form': form})
        return render(request,"home/search_results.html",{"filter":status,'form': form})
    else:
        form = SearchForm()
        return render(request,"home/search_results.html",{'form': form})

def home(request):
    return render(request, "home.html",{})

def gitlink(request):
    link = redirect('https://github.com/UVA-CS3240-S19/project-102-nautilus')
    return link

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})