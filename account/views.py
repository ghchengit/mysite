from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserInfo, UserProfile
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserInfoForm, UserForm

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Welcome! You have been login successfully!")
            else:
                return HttpResponse("Sorry. Your username or password is not right!")
        else:
            return HttpResponse("Invalid login")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})
        

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            newuser = user_form.save(commit=False)
            newuser.set_password(user_form.cleaned_data['password'])
            newuser.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = newuser
            new_profile = userprofile_form.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponse("successfully")
        else:
            return HttpResponse("invalid input")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form":user_form, "profile":userprofile_form})
        
        
def register0(request):
    if request.method == "POST":
        userprofile_form = UserProfileForm(request.POST)
        if userprofile_form.is_valid():
            newuser = userprofile_form.save(commit=False)
            newuser.set_password(userprofile_form.cleaned_data['password'])
            newuser.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("invalid input")
    else:
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form":userprofile_form })
        

@login_required(login_url="/account/login/")
def myself(request):
    user = request.user
    #user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, "account/myself.html", {"user":user, "userprofile":userprofile, "userinfo":userinfo})
    
    
@login_required(login_url="/account/login/")
def myself_edit(request):
    args = {}
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        userprofile_form = UserProfileForm(request.POST, instance=userprofile)
        userinfo_form = UserInfoForm(request.POST, instance=userinfo)
        if user_form.is_valid() and userprofile_form.is_valid() and userinfo_form.is_valid():
        #if True:
            user_form.save()
            userprofile_form.save()
            userinfo_form.save()
        #else:
            #raise forms.ValidationError("bad input!")
            return HttpResponseRedirect(reverse('account:my_information'))
    else:
        user_form = UserForm(instance=user)
        userprofile_form = UserProfileForm(instance=userprofile)
        userinfo_form = UserInfoForm(instance=userinfo)
        
    args["user_form"] = user_form
    args["userprofile_form"] = userprofile_form
    args["userinfo_form"] = userinfo_form
    
    return render(request, "account/myself_edit.html", args)
    

@login_required(login_url="/account/login/")
def my_image(request):
    if request.method == "POST":
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request, 'account/imagecrop.html',)

            

# Create your views here.
