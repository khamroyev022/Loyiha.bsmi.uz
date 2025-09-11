from django.urls import path
from . import views

urlpatterns = [
    path('', views.statistika_view, name='admin_dashboard'),
]
