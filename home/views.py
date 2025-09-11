from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import File,Profile,Message
from admin_dashboard.views import create_competition,create_news
from .models import yangilik,Tanlovlar

@login_required
def home_view(request):
    try:
        post_image = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:

        post_image = None


    news_list = yangilik.objects.all().order_by('created_at')[:6]
    competition_list = Tanlovlar.objects.all().order_by('created_at')[:6]
    
    context = {
        'post_image': post_image,
        'user': request.user,
        'competition_list': competition_list,
        'news_list': news_list,
    }
    return render(request, 'index.html', context)

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

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-sent_at')
    return render(request, 'messages.html', {'messages': messages})

@login_required
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



