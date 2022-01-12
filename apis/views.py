from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from conference_app.models import Conference, Talk, User
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/all-confrences/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array all the conferences'
        },
        {
            'Endpoint': '/conference/conference_id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single conference object'
        },
        {
            'Endpoint': 'conference/conference_id/talks',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array all the talks in a conference'
        },
        {
            'Endpoint': '/talk/talk_id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single talk object'
        },
        {
            'Endpoint': '/create-conference/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new conference with data sent in post request'
        },
        {
            'Endpoint': '/create-talk/confernce_id',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new talk with data sent in post request'
        },
        {
            'Endpoint': '/edit-conference/conference_id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update an existing conference'
        },
        {
            'Endpoint': '/edit-talk/talk_id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update an existing talk'
        },
        {
            'Endpoint': '/add-speaker/talk_id',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'add speakers to a talk'
        },
        {
            'Endpoint': '/add-participant/talk_id',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'add speakers to a talk'
        },
        {
            'Endpoint': '/remove-speaker/talk_id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'remove speakers from a talk'
        },
        {
            'Endpoint': '/remove-participant/talk_id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'remove participants from a talk'
        },
        {
            'Endpoint': '/get-speakers/talk_id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'get speakers in a talk'
        },
        {
            'Endpoint': '/get-participants/talk_id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'get participants in a talk'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getAllConferences(request):
    conferences = Conference.objects.all()
    serializer = ConferenceSerializer(conferences, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def a_conference(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    serializer = ConferenceSerializer(conference)
    return Response(serializer.data)

@api_view(['GET']) 
def a_talk(request, talk_id):
    talk = Talk.objects.get(id=talk_id)
    serializer = TalkSerializer(talk)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_conference(request):
    serializer = ConferenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_talk(request, conference_id):
    serializer = TalkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def edit_conference(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    if request.user.id == conference.host.id:
        serializer = ConferenceSerializer(conference, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("unathorized", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def edit_talk(request, talk_id):
    talk = Talk.objects.get(id=talk_id)
    if request.user.id == talk.host.id:
        serializer = TalkSerializer(talk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("unathorized", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_speaker(request, talk_id):
    talk = Talk.objects.get(pk=talk_id)
    print('This is talk:', talk)
    conference = Conference.objects.filter(pk=talk.conference.id)
    print('This is conference:', conference)
    if request.user.id == talk.host.id:
        serializer = AddSpeakerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("unathorized", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def remove_speaker(request, talk_id):
    talk = Talk.objects.get(pk=talk_id)
    print('This is talk:', talk)
    conference = Conference.objects.filter(pk=talk.conference.id)
    print('This is conference:', conference)
    if request.user.id == talk.host.id:
        serializer = SpeakerSerializer(data=request.data)
        if serializer.is_valid():
            talk.speakers.remove(serializer.data)
            talk.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("unathorized", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_participant(request, talk_id):
    talk = Talk.objects.get(pk=talk_id)
    print('This is talk:', talk)
    conference = Conference.objects.filter(pk=talk.conference.id)
    print('This is conference:', conference)
    if request.user.id == talk.host.id:
        serializer = AddParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('Serializer: ', serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("unathorized", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
# @permission_classes((IsAuthenticated,))
def remove_participant(request, talk_id):
    talk = Talk.objects.get(pk=talk_id)
    print('This is talk:', talk)
    conference = Conference.objects.filter(pk=talk.conference.id)
    print('This is conference:', conference)
    # if request.user.id == talk.host.id:
    serializer = ParticipantSerializer(data=request.data)
    if serializer.is_valid():
        talk.participants.remove(serializer)
        talk.save()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response("unathorized", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_talk_speakers(request, talk_id):
    talk = Talk.objects.get(id=talk_id)
    speakers = talk.speakers.all()
    serializer = UserSerializer(speakers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_talk_participants(request, talk_id):
    talk = Talk.objects.get(id=talk_id)
    participants = talk.participants.all()
    serializer = UserSerializer(participants, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_conference_talks(request, conference_id):
    conference = Conference.objects.get(id=conference_id)
    talks = Talk.objects.filter(conference=conference)
    serializer = TalkSerializer(talks, many=True)
    return Response(serializer.data)






