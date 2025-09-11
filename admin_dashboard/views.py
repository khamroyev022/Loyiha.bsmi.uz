
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import File, Profile, Message
from django.contrib.auth.models import User
from django.utils import timezone
from home.models import yangilik,Tanlovlar

@login_required
def statistika_view(request):
    total_users = User.objects.count()
    active_users = Profile.objects.filter(status='active').count()
    seven_days_ago = timezone.now() - timezone.timedelta(days=7)
    new_users = User.objects.filter(date_joined__gte=seven_days_ago).count()
    users_with_profile = User.objects.select_related('profile').prefetch_related('file_set').all()
    context = {
        'total_users': total_users,
        'active_users': active_users,
        'new_users': new_users,
        'users': users_with_profile,
    }

    return render(request, 'admin_dashboard.html', context)

@login_required
def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('discription')
        image = request.FILES.get('image')

        if title and subtitle and description and image:
            new_news = yangilik(
                title=title,
                subtitle=subtitle,
                discription=description,
                image=image
            )
            new_news.save()
            return render(request, 'admin_dashboard.html', {'success': True})
        else:
            return render(request, 'admin_dashboard.html', {'error': 'All fields are required.'})
        
@login_required
def create_competition(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if title  and description and image:
            new_competition = Tanlovlar(
                title=title,
                discription=description,
                image=image
            )
            new_competition.save()
            return render(request, 'admin_dashboard.html', {'success': True})
        else:
            return render(request, 'admin_dashboard.html', {'error': 'All fields are required.'})