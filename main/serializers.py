from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Category, Telemetry, Room, Device, Home, Scenarios


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'address', 'avatar']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializers()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]

class TelemetrySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Telemetry
        fields = ["temp","smoke","humidity","motion"]

class RoomSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Room
        fields = ['name','home']
class DeviceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Device
        fields = ['name','room',"uuid","Secret_key"]
class HomeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Home
        fields = ['name','user']

class ScenariosSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Scenarios
        fields = ['user','device',"scenario"]
