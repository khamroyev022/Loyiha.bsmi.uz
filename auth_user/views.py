from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate the user (you can use Django's built-in authentication)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username yoki parol xato')

    return render(request, 'login.html')
