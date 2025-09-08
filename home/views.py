from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.
def index_views(request):
    return render(request,'index.html')


from django.shortcuts import redirect

def logout_view(request):
    request.session.flush()
    response = HttpResponseRedirect('/login/')  # login sahifaga qaytarish
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
