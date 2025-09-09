from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import File,Profile
# Create your views here.
@login_required(login_url='/login/')  # faqat login bo‘lgan foydalanuvchi kira oladi
def home_view(request):
    post_image = Profile.objects.get(user=request.user)
    context = {'post_image': post_image}
    return render(request, 'index.html',context)


def log_out(request):
    logout(request)  # sessiyani tugatadi
    return redirect('login')
def message_views(request):
    return render(request,'message.html')


@login_required(login_url='/login/')
def person_data_views(request):
    person_data = Profile.objects.get(user=request.user)
    context = {
        'person_data': person_data,
        'user': request.user
        
        }
    return render(request,'person_data.html',context)







def file_upload_view(request):
    if request.method == 'POST':
        if request.FILES.get('uploade_file'):
            uploaded_file = request.FILES['uploade_file']
            File.objects.create(
                user=request.user,
                file=uploaded_file
            )
            return redirect('/home/?uploaded=1')

    return render(request, 'index.html')
