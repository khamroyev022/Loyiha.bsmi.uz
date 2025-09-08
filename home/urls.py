from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('logout/',views.log_out,name='logout'),
    path('message/',views.message_views,name='message'),
    path('person_data/',views.person_data_views,name='person_data'),
    path('upload/', views.file_upload_view, name='upload'),
]
