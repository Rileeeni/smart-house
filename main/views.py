from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView

from .models import Profile
from django.shortcuts import render
from rest_framework import generics
from .serializers import TelemetrySerializer, RoomSerializer, ProfileSerializers, DeviceSerializer
from .models import Telemetry, Room, Device
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


""""""
class TelemetryViewSet(viewsets.ModelViewSet):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Профиль"""
class Me(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Лист комнат"""
class ListRoom(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Лист Тревог"""
class AlarmList(generics.ListAPIView):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Лист сценариев"""
class ScenariosList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Добавть сценарий"""
class ScenariosAdd(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Сценарий по айди"""
class ScenariosById(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Лист Девайсов"""
class DeviceList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Добавить комнату"""
class RoomAdd(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Опред.девайс в опред. комнате """
class RoomIdDeviceByName(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Добавить девайс в комнату"""
class RoomAddDevice(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Телеметрия опред.комнаты"""
class RoomTelemetry(generics.ListAPIView):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated


"""Лист тревог"""
class AlarmsList(generics.ListAPIView):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = IsAuthenticated

