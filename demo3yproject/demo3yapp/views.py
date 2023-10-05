from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records=Record.objects.all()
    #check to see if logging in
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        #Authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you are logged in")
            return redirect('home')
        else:
            messages.success(request,"error logging in")
            return redirect('home')

    else:
     return render(request,'home.html',{'records':records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"logged out")
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            # login(request,user)
            messages.success(request,"you have registered")
            return redirect('login')
    else:
        form=SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html', {'form': form})

def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                # messages.success(request,"Record succesfully Added")
                return redirect('add_record')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request, "You must log in")
        return redirect('home')

# def login_user(request):
#     records = Record.objects.all()
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
#             # Authenticate
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "you are logged in")
#                 return redirect('home')
#             else:
#                 messages.success(request, "error logging in")
#                 return redirect('home')
#
#         else:
#             return render(request, 'home.html')
#
#
#     return render(request,'login.html',{'records':records})
def login_user(request):

    #check to see if logging in
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        #Authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you are logged in")
            return redirect('home')
        else:
            messages.success(request,"error logging in")
            return redirect('login')

    else:

         return render(request,'login.html')