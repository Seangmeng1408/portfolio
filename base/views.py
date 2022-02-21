import email
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Achievment
from django.shortcuts import redirect
from .forms import AchievmentForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.
def  Home(request):
    projectAchieve=Achievment.objects.all()
    return render(request,'base/main.html',{"projectAchieve":projectAchieve})


@login_required(login_url='/login/')
def Post(request):
    forms=AchievmentForm()
    if request.method=="POST":
        forms=AchievmentForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect("home")
    return render(request,'base/post.html',{"forms":forms})


@login_required(login_url='/login/')
def UpdatePost(request,slug):
    indProject=Achievment.objects.get(slug=slug)
    forms=AchievmentForm(instance=indProject)
    if request.method=="POST":
        forms=AchievmentForm(request.POST,request.FILES,instance=indProject)
        if forms.is_valid():
            forms.save()
            return redirect("home")
    return render(request,'base/post.html',{"forms":forms})


def Detail(request,slug):
    indProject=Achievment.objects.get(slug=slug)
    if( indProject.Readable!=True):
        return redirect('home')
    return render(request,'base/detail.html',{"indProject":indProject})



@login_required(login_url='/login/')
def Delete(request,slug):
    indProject=Achievment.objects.get(slug=slug)
    print(indProject)
    if request.method=="POST":
        indProject.delete()
        return redirect("home")
    return render(request,"base/delete.html",{"indProject":indProject})

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request,"Your Password or User Name not correct!")
            return redirect("login")
    return render(request,"base/login.html",{})


    
@login_required(login_url='/login/')
def Logout(request):
    logout(request)
    return redirect("home")


def Contact(request):
    return render(request,"base/contact.html")

def SendEmail(request):
    if request.method=="POST":
        template=render_to_string("base/email_template.html",{
            'name':request.POST['firstname']+" "+request.POST['lastname'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })
        email=EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ["bongmeng60@gmail.com"]
        )
        email.fail_silently=False
        email.send()
    return render(request,"base/sendsuccess.html")


def ERROR_404(request,exception):
    return render(request,"base/error_404.html",{})