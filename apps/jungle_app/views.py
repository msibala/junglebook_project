# from typing import _get_type_hints_obj_allowed_types
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
# import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
    return render(request, 'jungle_app/login.html')

from .models import User
from .models import User
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')

    # hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    # decoded_hash = hashed.decode('utf-8')

    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=decoded_hash, birth_year=request.POST['birth_year'])
    print(f" user {user.id}")
    # request.session['u_id'] = user.id
    # request.session['u_fname'] = user.first_name

    return redirect('/wall')

        
def login(request):
    print(request.data)
    user_list = User.objects.filter(email=request.POST['email'])
    user = user_list[0]
    print(user.id)

    # if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
    #     context = {
    #         'user': user
    #     }

    
    return render(request, 'jungle_app/wall.html')

def home(request):
    if request.session.get('user', False):
        return render(request, 'jungle_app/wall.html')
    else:
        return render(request, 'jungle_app/login.html')




def wall(request):
    context = {
        'posts' : Message.objects.all(),
    }
    return render(request, 'jungle_app/wall.html', context)

def post(request):
    message = Message.objects.create(message=request.POST['message'], messager=User.objects.get(id=request.session['u_id']))
    print(message.id)
    return redirect('/wall')

    
def comment(request):
    comment = Comment.objects.create(comment=request.POST['comment'], commentor=User.objects.get(id=request.session['u_id']), post=Message.objects.get(id=request.POST['post_id']))
    print(comment.id)
    return redirect('/wall')

def logout(request):
    return render(request,"jungle_app/logout.html")

def delmsg(request, id):
    Message.objects.get(id=id).delete()
    return redirect('/wall')

def delcom(request, id):
    Comment.objects.get(id=id).delete()
    return redirect('/wall')

def animals(request):
    return render(request, 'jungle_app/animals.html')

def land(request):
    return render(request, 'jungle_app/land.html')

def ocean(request):
    return render (request, 'jungle_app/ocean.html')  

def aerial(request):
    return render (request, 'jungle_app/aerial.html')  

def food(request):
    return render (request, 'jungle_app/food.html')  

def anatomy(request):
    return render(request, 'jungle_app/anatomy.html')

def register(request):
    return render(request, 'jungle_app/wall.html')

