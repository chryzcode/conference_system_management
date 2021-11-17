from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='get-routes'),
    path('all-confrences/', views.getAllConferences, name='get-all-conferences'),
    path('conference/<int:conference_id>/', views.a_conference, name='get-conference'),
    path('talk/<int:talk_id>/', views.a_talk, name='get-talk'),
    path('create-conference/', views.create_conference, name='create-conference'),
    path('create-talk/', views.create_talk, name='create-talk'),
]