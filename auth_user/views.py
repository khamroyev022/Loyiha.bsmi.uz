from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:   # Avval user mavjudligini tekshiramiz
            login(request, user)

            if user.is_superuser:   # Agar admin bo‘lsa
                return redirect('/admin/')
            else:                   # Oddiy foydalanuvchi
                return redirect('/home/')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'login.html')
