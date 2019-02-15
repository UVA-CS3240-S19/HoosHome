from django.shortcuts import render,redirect

def home(request):
    return render(request, "home.html",{})

def gitlink(request):
    link = redirect('https://github.com/UVA-CS3240-S19/project-102-nautilus')
    return link