from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



def home_page(request):
    return render(request, 'jungle_app/home_page.html')

def land(request):
    return render(request, 'jungle_app/land.html')

def ocean(request):
    return render (request, 'jungle_app/ocean.html')  

def wing(request):
    return render (request, 'jungle_app/wing.html')  

def login(request):
    return render(request, 'jungle_app.login.html')

from .models import User
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')