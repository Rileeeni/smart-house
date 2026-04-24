from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Profile
from django.shortcuts import render
from rest_framework import generics
from .serializers import TelemetrySerializer, RoomSerializer, ProfileSerializers, DeviceSerializer,ScenariosSerializer
from .models import Telemetry, Room, Device,Scenarios
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from .models import Telemetry
from .serializers import TelemetrySerializer


class MySecureView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


class TelemetryAPIView(generics.ListAPIView):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class TelemetryViewSet(viewsets.ModelViewSet):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class Me(APIView):
    """Профиль"""
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated

    def get(self, request):
        serializer = ProfileSerializers(request.user)
        return Response(serializer.data)



class ListRoom(generics.ListAPIView):
    """Лист комнат"""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class AlarmList(generics.ListAPIView):
    """Лист Тревог"""
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class ScenariosList(generics.ListAPIView):
    """Лист сценариев"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class ScenariosAdd(CreateAPIView):
    """Добавить сценарий"""
    queryset = Scenarios.objects.all()
    serializer_class = ScenariosSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class ScenariosById(RetrieveUpdateDestroyAPIView):
    """Сценарий по айди"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class DeviceList(generics.ListAPIView):
    """Лист Девайсов"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class RoomAdd(CreateAPIView):
    """Добавить комнату"""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class RoomIdDeviceByName(ListAPIView):
    """Опред.девайс в опред. комнате """
    queryset = Room.objects.all()
    serializer_class = DeviceSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated
    def get_queryset(self):
        room_id = self.kwargs['room_id']
        device_name = self.kwargs['device_name']
        return Device.objects.filter(room_id=room_id, name=device_name)



class RoomAddDevice(CreateAPIView):
    """Добавить девайс в комнату"""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class RoomTelemetry(generics.ListAPIView):
    """Телеметрия опред.комнаты"""
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated



class AlarmsList(generics.ListAPIView):
    """Лист тревог"""
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated

