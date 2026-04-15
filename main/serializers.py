from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Category, Telemetry


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

