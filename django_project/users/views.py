from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.instance.is_staff = True 
            form.instance.is_superuser = True 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm() 
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')