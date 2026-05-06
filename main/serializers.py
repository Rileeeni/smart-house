from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .models import Profile, Category, Telemetry, Room, Device, Home, Scenarios


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'avatar',"password"]
    def validate_email(self, email):
        if not email.strip():
            raise serializers.ValidationError("email не может быть пустым")
        return email
    def validate_password(self, password):
        if not password.strip():
            raise serializers.ValidationError("password не может быть пустым")
        return password
    def create(self, validated_data):
        password = validated_data.pop('password')
        profile = Profile.objects.create(validated_data)
        profile.set_password(validated_data['password'])
        profile.save()
        return profile


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializers()
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        def validate_name(self,value):
            if not value.strip():
                raise  serializers.ValidationError("Название дома не может быть пустым")
            if len(value.strip()) < 4:
                raise serializers.ValidationError("Название дома слишком короткое")

class TelemetrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Telemetry
        fields = ["temperature","smoke","humidity","motion","timestamp"]
        def validate_temperature(self, temperature):
            if (temperature.strip()) < -10:
                raise serializers.ValidationError("Температура не может быть ниже -10")
            if (temperature.strip()) > 40:
                raise serializers.ValidationError("Температура не может быть выше 40")
            return temperature
        def validate_humidity(self,humidity):
            if humidity < 0 or humidity > 100:
                raise serializers.ValidationError(
                    "Влажность должна быть в диапазоне от 0 до 100"
                )
            return humidity


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name','home']
        def validate_name(self,value):
            if not value.strip():
                raise  serializers.ValidationError("Название комнаты не может быть пустым")
        def validate_room(self,data):
            if Room.objects.filter(
                name=data["name"]
            ).exists():
                raise serializers.ValidationError(
                    "Комната с таким названием уже есть"
                )


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name','room',"uuid","secret_key"]
        extra_kwargs = {
            'secret_key': {'write_only': True},
            'room': {"read_only": True}
        }

    def validate_secret_key(self, value):
        if len(value.strip()) < 12:
            raise serializers.ValidationError("secret_key слишком короткий")
        if not value.strip():
            raise serializers.ValidationError("secret_key не может быть пустым")
        return value

    def validate_name(self, value):
        if len(value.strip()) < 4:
            raise serializers.ValidationError("Название девайса слишком короткое")
        if not value.strip():
            raise serializers.ValidationError("Название девайса не может быть пустым")
        return value

    def validate_room(self, data):
        if name.objects.filter(
                name=data["name"]
        ).exists():
            raise serializers.ValidationError(
                "Комната с таким название уже есть"
            )
        return data



class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['name','user']
        def validate_name(self,value):
            if not value.strip():
                raise  serializers.ValidationError("Название дома не может быть пустым")
            if len(value.strip()) < 4:
                raise serializers.ValidationError("Название девайса слишком короткое")
            return value


class ScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenarios
        fields = ['user','device',"scenario"]
        def validate_device(self,device):
            if not device.strip():
                raise  serializers.ValidationError("Список девайсов не может быть пустым не может быть пустым")
        def validate_scenario(self,scenario):
            if not scenario.strip():
                raise  serializers.ValidationError("Сценарий не может быть пустым не может быть пустым")
