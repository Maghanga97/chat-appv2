from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'ChatRooms'

class Messages(models.Model):
    text_msg = models.CharField(max_length=10000)
    time_stamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Messages'