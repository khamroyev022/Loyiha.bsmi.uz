from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.
def index_views(request):
    return render(request,'index.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html')
