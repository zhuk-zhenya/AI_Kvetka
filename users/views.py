from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'users/login.html')

def registration(request):
    return render(request, 'users/register.html')

def profile(request):
    return render(request, 'users/profile.html')

def logout(request):
    pass