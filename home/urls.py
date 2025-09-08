from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_views,name='home'),
    path('logout/',views.logout_view,name='logout'),
    path('message/',views.message_views,name='message'),
    path('person_data/',views.person_data_views,name='person_data'),
]
