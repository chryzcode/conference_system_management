from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

#custom login view
def loginPage(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
             
    return render(request,'registration/login.html', context)

#custom register view
def registerPage(request):
    form = SignupForm
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect ('home')
        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'registration/register.html', {'form':form})

#custom logout view
def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    conferences = Conference.objects.all()
    context = {'conferences':conferences}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def createConference(request):
    form = ConferenceForm
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user  
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'An error occured during conference creation')

    return render(request, 'conference.html', {'form':form})


@login_required(login_url='login')
def editConference(request, conference_id):
    conference = Conference.objects.get(pk=conference_id)
    if request.user == conference.host:
        form = ConferenceForm(instance=conference)
        if request.method == 'POST':
            form = ConferenceForm(request.POST, instance=conference)
            if form.is_valid():
                form.save()
                return redirect ('home')
        return render(request, 'conference.html', {'form':form})
    else:
        return redirect('home')

def viewConference(request, conference_id):
    conference = Conference.objects.get(pk=conference_id)
    talks = Talk.objects.filter(conference=conference)
    context = {'conference':conference, 'talks':talks}
    return render(request, 'view-conference.html', context)

@login_required(login_url='login')
def createTalk(request, conference_id):
    form = TalkForm
    conference = Conference.objects.get(pk=conference_id)
    if request.method == 'POST':
        form = TalkForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user 
            form.conference = conference
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'An error occured during talk creation')

    return render(request, 'talk.html', {'form':form})


@login_required(login_url='login')
def editTalk(request, talk_id):
    talk = Talk.objects.get(pk=talk_id)
    if request.user == talk.host:
        form = TalkForm(instance=talk)
        if request.method == 'POST':
            form = TalkForm(request.POST, instance=talk)
            if form.is_valid():
                form.save()
                return redirect ('home')
        return render(request, 'talk.html', {'form':form})
    else:
        return redirect('home')

@login_required(login_url='login')
def addSpeaker(request, talk_id):
    form = AddSpeakerForm
    talk = Talk.objects.get(pk=talk_id)
    if request.user == talk.host:
        if request.method == 'POST':
            speaker = request.POST.get('speakers')
            talk.speakers.add(speaker)
            return redirect ('view-talk', talk_id=talk.id)
        return render(request, 'speaker.html', {'form':form})
    else:
        return redirect('home')

@login_required(login_url='login')
def removeSpeaker(request, talk_id):
    form = RemoveSpeakerForm
    talk = Talk.objects.get(pk=talk_id)
    if request.user == talk.host:
        if request.method == 'POST':
            speaker = request.POST.get('speakers')
            talk.speakers.remove(speaker)
            return redirect ('view-talk', talk_id=talk.id)
        return render(request, 'speaker.html', {'form':form})
    else:
        return redirect('home')

def viewTalk(request, talk_id):
    talk = Talk.objects.get(pk=talk_id)
    conference = talk.conference
    context = {'conference':conference, 'talk':talk}
    return render(request, 'view-talk.html', context)

@login_required(login_url='login')
def addParticipant(request, talk_id):
    form = AddParticipantForm
    talk = Talk.objects.get(pk=talk_id)
    if request.user == talk.host:
        if request.method == 'POST':
            participant = request.POST.get('participants')
            talk.participants.add(participant)
            return redirect ('view-talk', talk_id=talk.id)
        return render(request, 'participants.html', {'form':form})
    else:
        return redirect('home')


@login_required(login_url='login')
def removeParticipant(request, talk_id):
    form = RemoveParticipantForm
    talk = Talk.objects.get(pk=talk_id)
    if request.user == talk.host:
        if request.method == 'POST':
            participant = request.POST.get('participants')
            talk.participants.remove(participant)
            return redirect ('view-talk', talk_id=talk.id)
        return render(request, 'participants.html', {'form':form})
    else:
        return redirect('home')


def profile(request, username):
    user = User.objects.get(username=username)
    conferences = Conference.objects.filter(host=user)
    context = {'user':user, 'conferences':conferences}
    return render(request, 'profile.html', context)

