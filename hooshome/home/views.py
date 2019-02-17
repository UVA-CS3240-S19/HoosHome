from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

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