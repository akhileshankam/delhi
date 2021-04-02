from datetime import datetime
from sqlite3 import IntegrityError
import time
import razorpay
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages, auth
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from . models import employee

import time


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template




def home(request):
    if request.user.is_authenticated:
       return render(request,'welcome1.html')
    else:
        return render(request,'home.html')
def signupform(request):
    return render(request,'signupform.html')
def register(request):
    if request.method=="POST":

        username=request.POST['username']
        mobileno=request.POST['empoff']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if User.objects.filter(username=username).exists():
            messages.success(request,"username already exists")
            return render(request,'signupform.html')
        else:
                if cpassword==password:
                    if username and password:
                        x=User.objects.create_user(username=username,password=password)
                        x.save()
                        y=employee(empname=username,mobileno=mobileno)
                        y.save()
                        return render(request,'confirmation.html')
                    else:
                        messages.success(request,"enter all fields")
                        return render(request,'signupform.html')
                else:
                    messages.success(request,"passwords didn't match")
                    return render(request,'signupform.html')
def loginform(request):
    return render(request,'loginform.html')
l=[0]
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username and password:
            user=authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return render(request,'welcome1.html')

            else:
                 messages.success(request,"invalid username or password")
                 return render(request,'loginform.html')
        else:
            messages.success(request, "enter all fields")
            return render(request, 'loginform.html')
def logout(request):

    auth.logout(request)
    return render(request,'home.html')
def calculate(request):
    if request.user.is_authenticated:
        x = request.POST['x']
        n = request.POST['n']
        x=int(x)
        n=int(n)
        a = 0
        for i in range(n):
             a = 1 / x ** n + a
        return HttpResponse(a)
def task2(request):
    l=[2,3,10,15,26,35,50,63]
    x=l[len(l)-1]+l[len(l)-2]-l[len(l)-3]+4
    return x


def task3(request,x,y,a,b):
    m=(x+1/y)**a
    n=(x-1/y)**b
    o=(y+1/x)**a
    p=(y-1/x)**b
    z=(m*n)/(o*p)
    return z







