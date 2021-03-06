from django import urls
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import signup
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

#HOME PAGE OF WEBSITE

def dashboard(request):
    return render(request,'enroll/dashboard.html')




#AUTHINTICATED PAGES

def user_register(request):
    if request.method=="POST":
        form=signup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations: your account have been sucessfully created')
    else:
        form=signup()
    return render(request,'enroll/register.html',{'fm':form})

#user_login:-

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/prof/')
        else:
            form=AuthenticationForm()
        return render(request,'enroll/login.html',{'fm':form})
    else:
        return HttpResponseRedirect('/prof/')

#user_logout:-

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/log/')


#PROFILE OF WEBSITE AND INSIDE IT ALL APPLICATION:-

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html')
    else:
        return HttpResponseRedirect('/log/')
    

#another page which is inside the profile page

