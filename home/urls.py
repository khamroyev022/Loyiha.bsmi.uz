from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index_views,name='home'),
    path('logout/',views.logout_view,name='logout'),
]
