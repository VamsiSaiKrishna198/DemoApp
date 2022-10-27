from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from pymongo import MongoClient

from chatapp.models import NewUserform


def newuser(request):
    if request.method == 'POST':
        form= NewUserform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'/home')
    else:
        form= NewUserform()
        return render(request,'newuser.html',{'form': form})

def loginpage(request):
    if request.method == 'POST':
        form= AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('home1.html')
    else:
        form = AuthenticationForm(data=request.POST)
    return render(request,'loginpage.html',{'form': form})

@csrf_exempt
def homepage(request):
    print(request.POST.dict())
    n=request.POST.get('search')
    print(n)
    name=str(n).lower()
    if name =='mumbai':
        return render(request,'mumbai.html')
    elif name =='kolkata':
        return render(request,'kolkata.html')
    elif name =='hyderabad':
        return render(request,'hyderabad.html')
    if name =='visakhapatnam':
        return render(request,'visakhapatnam.html')
    else:
        template=loader.get_template('home.html')
        return HttpResponse(template.render())

def homepage1(request):
    template=loader.get_template('home1.html')
    return HttpResponse(template.render())

def homepage2(request):
    if request.method =='POST' :
        name=request.GET.get('name','This is the default value')
        if name == 'kolkate':

            return render(request,'newuser.html')

def reservation(request):
    template=loader.get_template('reservation.html')
    return HttpResponse(template.render())

def mumbai(request):
    template=loader.get_template('hyderabad.html')
    return HttpResponse(template.render())

def payment(request):
    template=loader.get_template('payment.html')
    return HttpResponse(template.render())