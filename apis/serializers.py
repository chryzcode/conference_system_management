from rest_framework.serializers import ModelSerializer
from conference_app.models import *
from rest_framework import serializers

class ConferenceSerializer(ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'

class TalkSerializer(ModelSerializer):
    class Meta:
        model = Talk
        fields = '__all__'
 
 
class AddSpeakerSerializer(ModelSerializer):
    class Meta:
        model = Talk
        fields = ['speakers']

class SpeakerSerializer(ModelSerializer):
    speakers = AddSpeakerSerializer(many=True)
    class Meta:
        model = Talk
        fields = ['speakers']

class AddParticipantSerializer(ModelSerializer):
    class Meta:
        model = Talk
        fields = ('participants',)

class ParticipantSerializer(ModelSerializer):
    participants = AddParticipantSerializer(many=True)
    class Meta:
        model = Talk
        fields = ('participants',)