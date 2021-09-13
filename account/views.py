from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            use=form.save()
            user=form.cleaned_data.get('username')
            login(request, use)
            messages.success(request, 'Account was created for ' + user)
            return redirect('home')

    context={'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = AuthenticationForm()
    context={'form':form}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')
   


