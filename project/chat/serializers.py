from .models import ChatUser, Room, Message
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatUser
        fields = ["id", "short_name", "avatar"]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["room", "text", "user", "created_at"]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "host", "current_users"] #"messages", "last_message"
  