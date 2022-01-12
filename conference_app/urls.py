from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('create-conference/', views.createConference, name='create-conference'),
    path('conference/<str:conference_id>/', views.viewConference, name='view-conference'),
    path('edit-conference/<str:conference_id>/', views.editConference, name='edit-conference'),
    path('create-talk/<str:conference_id>/', views.createTalk, name='create-talk'),
    path('talk/<str:talk_id>/', views.viewTalk, name='view-talk'),
    path('edit-talk/<str:talk_id>/', views.editTalk, name='edit-talk'),
    path('add-speaker/<str:talk_id>/', views.addSpeaker, name='add-speaker'),
    path('remove-speaker/<str:talk_id>/', views.removeSpeaker, name='remove-speaker'),
    path('add-participants/<str:talk_id>/', views.addParticipant, name='add-participant'),
    path('remove-participant/<str:talk_id>/', views.removeParticipant, name='remove-participant'),
    path('profile/<username>/', views.profile, name='profile'),
    ]   