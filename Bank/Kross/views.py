from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('login')
        else:
            form = RegisterForm()
        return render(request, 'bank/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'bank/register.html', {'form': form})
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid Credentials')
    # Render the login page for GET requests or after failed login
    return render(request, 'bank/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def welcome_view(request):
    return render(request,'bank/welcome.html',{'user': request.user})