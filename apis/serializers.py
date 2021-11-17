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
        # depth = 1

# class SpeakerSerializer(ModelSerializer):
#     class Meta:
#         model = Talk
#         fields = ['speakers']



# class ParticipantSerializer(ModelSerializer):
#     class Meta:
#         model = Talk
#         fields = ('participants')