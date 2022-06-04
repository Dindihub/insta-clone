
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,LoginUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# views for html
def index(request):
    
    return render(request, 'index.html')

def register(request):
    form=CreateUserForm

    if request.method =='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("registration successful"))
        
            return redirect('login')

    return render(request,'registration/register.html',{'form':form})

def login_user(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('login success!')
            return redirect('home')
        
    context={}
    return render(request,'registration/login.html',context)
