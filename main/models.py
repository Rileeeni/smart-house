from django.db import models
from django.contrib.auth.models import User
import uuid
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

class Home (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Room(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Device(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    secret_key = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
