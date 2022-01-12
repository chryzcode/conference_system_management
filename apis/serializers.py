from rest_framework.serializers import ModelSerializer
from conference_app.models import *
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name')

class ConferenceSerializer(ModelSerializer):
    host = UserSerializer(read_only=True)
    class Meta:
        model = Conference
        fields = ('id', 'host', 'title', 'description', 'start_date', 'end_date')

class TalkSerializer(ModelSerializer):
    speakers = UserSerializer(many=True, read_only=True)
    participants = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Talk
        fields = ('id', 'title', 'description', 'speakers', 'participants', 'date_time', 'duration')
 
 
class AddSpeakerSerializer(ModelSerializer):
    speakers = serializers.EmailField()
    class Meta:
        model = Talk
        fields = ['speakers']

class RemoveSpeakerSerializer(ModelSerializer):
    speakers = serializers.EmailField()
    class Meta:
        model = Talk
        fields = ['speakers']

class ParticipantSerializer(serializers.Serializer):
    participant = serializers.EmailField()

class SpeakerSerializer(ModelSerializer):
    speaker = serializers.EmailField()