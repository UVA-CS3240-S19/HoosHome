from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, ListView
from .forms import SignUpForm, SearchForm, ListingForm
from .models import Listing
from django.shortcuts import get_object_or_404


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


def search(request):
    if request.method == 'POST':
        key = request.POST['keyword']
        beds = request.POST.get('beds',False)
        baths = request.POST.get('baths',False)
        if key == "" and beds == "Number of Bedrooms" and baths == "Number of Bathrooms":
            return render(request, "home/search_results.html" )
        status = Listing.objects.filter(address__icontains=(key))
        if beds == "1 bed":
            status = status.filter(beds=1)
        elif beds == "2 beds":
            status = status.filter(beds=2)
        elif beds == "3 beds":
            status = status.filter(beds=3)
        elif beds == "3+ beds":
            status = status.filter(beds__gte=3)

        if baths == "1 bath":
            status = status.filter(baths=1)
        elif baths == "2 baths":
            status = status.filter(baths=2)
        elif baths == "3 baths":
            status = status.filter(baths=3)
        elif baths == "3+ baths":
            status = status.filter(baths__gte=3)

        return render(request, "home/search_results.html", {"filter": status})
    else:
        return render(request, "home/search_results.html")

def individual(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, "home/listing_individual.html", {"listing": listing})

def home(request):
    if request.method == 'POST':
        key = request.POST['keyword']
        beds = request.POST.get('beds',False)
        baths = request.POST.get('baths',False)
        if key == "" and beds == "Number of Bedrooms" and baths == "Number of Bathrooms":
            return render(request, "home.html" )
        status = Listing.objects.filter(address__icontains=(key))
        if beds == "1 bed":
            status = status.filter(beds=1)
        elif beds == "2 beds":
            status = status.filter(beds=2)
        elif beds == "3 beds":
            status = status.filter(beds=3)
        elif beds == "3+ beds":
            status = status.filter(beds__gte=3)

        if baths == "1 bath":
            status = status.filter(baths=1)
        elif baths == "2 baths":
            status = status.filter(baths=2)
        elif baths == "3 baths":
            status = status.filter(baths=3)
        elif baths == "3+ baths":
            status = status.filter(baths__gte=3)

        return render(request,"home/listing_filter.html", {"all_listings": status})
    else:
        return render(request, "home.html")



def gitlink(request):
    link = redirect('https://github.com/UVA-CS3240-S19/project-102-nautilus')
    return link

def ListingCreateView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/listings')
    else:
        form = ListingForm()
    return render(request, 'home/listing_form.html', {'form': form})

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
