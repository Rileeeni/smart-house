from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Category, Telemetry, Room, Device, Home, Scenarios


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'address', 'avatar']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializers()
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]

class TelemetrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Telemetry
        fields = ["temperature","smoke","humidity","motion"]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name','home']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name','room',"uuid","secret_key"]

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['name','user']

class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenarios
        fields = ['user','device',"scenario"]
