from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *
from .models import *
# Create your views here.


class UserSerializer(viewsets.ModelViewSet):
   '''класс пользователя, для чтения и создания'''
   queryset = ChatUser.objects.all()
   serializer_class = UserSerializer


class RoomSerializer(viewsets.ModelViewSet):
   '''класс комнат, чтение, редактированеи, удаление'''
   queryset = Room.objects.all()
   serializer_class = RoomSerializer


class MessageSerializer(viewsets.ModelViewSet):
   '''класс сообщений, чтение, редактированеи, удаление'''
   queryset = Message.objects.all()
   serializer_class = MessageSerializer      