from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout,get_user_model
from .forms import SignupForm, LoginForm
from django.contrib import messages

User_info=get_user_model()

# Create your views here.
# user login
def login(request):
    
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('dashboard')
            else:
                messages.add_message(request, messages.INFO, "Incorrect Password or Email. Please check the details !")
                return redirect('login')

            
    else:
        form=LoginForm()
            
    return render(request,"login.html",{'form':form})

  
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()

    return render(request, "signup.html", {'form': form})

def dashboard(request):
    return render(request,"dashboard.html")

def logout(request):
    auth_logout(request)
    return redirect('login')

