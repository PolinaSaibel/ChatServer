from django.db import models
from django.contrib.auth.models import User

class ChatUser(models.Model):
    """ модель пользователя """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author")
    short_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    avatar = models.ImageField(upload_to='images/profile/', null=True, blank=True)

    # def get_absolute_url(self):
    #     return reverse('author_pofile', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.user)


class Room(models.Model):
    """комнаты"""
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    host = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    current_users = models.ManyToManyField(ChatUser, through='RoomUsers', related_name="current_rooms", blank=True)

    def __str__(self):
        return f"Room({self.name} {self.host})"


class RoomUsers(models.Model):
    '''таблица связи комнат и пользователей'''
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Message(models.Model):
    """ сообщения """
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message({self.user} {self.room})"
