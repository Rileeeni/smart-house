from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models import ManyToManyField


#from .serializers import TelemetrySerializer


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
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

class Telemetry(models.Model):
   temperature = models.FloatField()
   smoke = models.BooleanField()
   humidity = models.FloatField()
   motion = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Scenarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = ManyToManyField(Device)
    scenario = models.JSONField()





