from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully Loged in")
            return redirect('dashboard')
        else:
            messages.error(request, 'Credentials are wrong! Please try again')
            return redirect('login') 
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['username']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already in use!')
                return redirect('register') 
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already in use!')
                    return redirect('register') 
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, "Successfully registered")
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, "Successfully registered")
                    request.redirect('login')

        else:
            messages.error(request, 'Password do not match')
            return redirect('register') 
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('home')
    else:
        return redirect('dashboard')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')