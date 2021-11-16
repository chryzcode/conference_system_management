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
    ]   