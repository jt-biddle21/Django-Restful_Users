from django.shortcuts import render, redirect
from .models import User


def index(request):
    context = {
        "all": User.objects.all(),
    }
    return render(request, 'restful_app/index.html', context)


def new(request):
    return render(request, 'restful_app/adduser.html')


def add(request):
    if request.method == "POST":
        User.objects.create(fname=request.POST['first'], lname=request.POST['last'], email=request.POST['email'])
    else:
        redirect('/')
    return redirect('/')


def delete(request, number):
    User.objects.filter(id=number).delete()
    return redirect('/')


def show(request, number):
    usercontext = {
        "user": User.objects.filter(id=number),
    }
    return render(request, 'restful_app/showuser.html', usercontext)


def abouttoedit(request, number):
    editcontext = {
        "euser": User.objects.filter(id=number),
    }
    return render(request, 'restful_app/edituser.html', editcontext)


def edit(request, number):
    useredit = User.objects.get(id=number)
    useredit.fname = request.POST['newfname']
    useredit.lname = request.POST['newlname']
    useredit.email = request.POST['newemail']
    useredit.save()
    return redirect('/')
