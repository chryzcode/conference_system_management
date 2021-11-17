from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from conference_app.models import *
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
            'Endpoint': '/conference_id/talks',
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
            'Endpoint': '/create-talk/',
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
            'Endpoint': '/add-speaker/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'add speakers to a talk'
        },
        {
            'Endpoint': '/add-participant/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'add speakers to a talk'
        },
        {
            'Endpoint': '/remove-speaker/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'remove speakers from a talk'
        },
        {
            'Endpoint': '/remove-participant/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'remove participants from a talk'
        },
    ]
    return Response(routes)