from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'address', 'avatar']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializers()