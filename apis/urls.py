from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='get-routes'),
    path('all-confrences/', views.getAllConferences, name='get-all-conferences'),
    path('conference/<str:conference_id>/', views.a_conference, name='get-conference'),
    path('talk/<str:talk_id>/', views.a_talk, name='get-talk'),
    path('create-conference/', views.create_conference, name='create-conference'),
    path('create-talk/<str:conference_id>/', views.create_talk, name='create-talk'),
    path('edit-conference/<str:conference_id>/', views.edit_conference, name='edit-conference'),
    path('edit-talk/<str:talk_id>/', views.edit_talk, name='edit-talk'),
    path('add-speaker/<str:talk_id>/', views.add_speaker, name='add-speaker'),
    path('get-speakers/<str:talk_id>/', views.get_talk_speakers, name='get-speakers'),
    path('get-participants/<str:talk_id>/', views.get_talk_participants, name='get-participants'),
    path('conference/<str:conference_id>/talks/', views.get_conference_talks, name='get-conference-talks'),
    path('remove-speaker/<talk_id>/', views.remove_speaker, name='remove-speaker'),
    path('add-participant/<str:talk_id>/', views.add_participant, name='add-participant'),
    path('remove-participant/<str:talk_id>/', views.remove_participant, name='remove-participant'),
]