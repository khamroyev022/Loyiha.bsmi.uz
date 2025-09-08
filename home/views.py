from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import File
# Create your views here.
@login_required(login_url='/login/')  # faqat login bo‘lgan foydalanuvchi kira oladi
def home_view(request):
    return render(request, 'index.html')


def log_out(request):
    logout(request)  # sessiyani tugatadi
    return redirect('login')
def message_views(request):
    return render(request,'message.html')

def person_data_views(request):
    return render(request,'person_data.html')




# def file_uplode_views(request):
#     if request.method == 'POST':
#         print("POST keldi ✅")
#         print("User:", request.user, " | Auth:", request.user.is_authenticated)
#         print("FILES:", request.FILES)

#         if request.FILES.get('uploade_file'):
#             uploaded_file = request.FILES['uploade_file']
#             obj = File.objects.create(
#                 user=request.user,
#                 file=uploaded_file
#             )
#             print("Saqlangan obyekt:", obj)
#             return render(request, 'index.html', {"success": True})

#     return render(request, 'index.html', {"success": False})

def file_upload_view(request):
    if request.method == 'POST':
        if request.FILES.get('uploade_file'):
            uploaded_file = request.FILES['uploade_file']
            File.objects.create(
                user=request.user,
                file=uploaded_file
            )
            # 🔴 POSTdan keyin redirect
            return redirect('/home/?uploaded=1')

    return render(request, 'index.html')
