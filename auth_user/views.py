from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:   
            login(request, user)
            if user.is_superuser:  
                return redirect('/admin/')
            else:                   
                return redirect('home') 
        else:
            messages.error(request, 'Username yoki parol noto‘g‘ri!')

    return render(request, 'login.html')