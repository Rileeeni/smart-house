from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Device, Profile, Room, Scenarios, Telemetry
from .serializers import (
    DeviceSerializer,
    ProfileSerializers,
    RoomSerializer,
    ScenariosSerializer,
    TelemetrySerializer,
)


class AuthenticatedMixin:
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]


class MySecureView(AuthenticatedMixin, APIView):
    pass


class TelemetryAPIView(AuthenticatedMixin, generics.ListAPIView):
    serializer_class = TelemetrySerializer

    def get_queryset(self):
        return Telemetry.objects.filter(
            device__room__home__user=self.request.user
        ).select_related("device", "device__room")


class TelemetryViewSet(AuthenticatedMixin, viewsets.ModelViewSet):
    serializer_class = TelemetrySerializer

    def get_queryset(self):
        return Telemetry.objects.filter(
            device__room__home__user=self.request.user
        ).select_related("device", "device__room")


class Me(AuthenticatedMixin, APIView):
    def get(self, request):
        profile, _ = Profile.objects.get_or_create(
            username=request.user,
            defaults={"email": request.user.email or f"{request.user.username}@example.com"},
        )
        serializer = ProfileSerializers(profile)
        return Response(serializer.data)


class ListRoom(AuthenticatedMixin, generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.filter(home__user=self.request.user).select_related("home")


class AlarmList(AuthenticatedMixin, generics.ListAPIView):
    serializer_class = TelemetrySerializer

    def get_queryset(self):
        return Telemetry.objects.filter(
            device__room__home__user=self.request.user
        ).filter(Q(smoke=True) | Q(motion=True)).select_related("device", "device__room")


class ScenariosList(AuthenticatedMixin, generics.ListAPIView):
    serializer_class = ScenariosSerializer

    def get_queryset(self):
        return Scenarios.objects.filter(user=self.request.user).prefetch_related("device")


class ScenariosAdd(AuthenticatedMixin, generics.CreateAPIView):
    serializer_class = ScenariosSerializer

    def get_queryset(self):
        return Scenarios.objects.filter(user=self.request.user)


class ScenariosById(AuthenticatedMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScenariosSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def get_queryset(self):
        return Scenarios.objects.filter(user=self.request.user).prefetch_related("device")


class DeviceList(AuthenticatedMixin, generics.ListAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.filter(room__home__user=self.request.user).select_related("room")


class RoomAdd(AuthenticatedMixin, generics.CreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.filter(home__user=self.request.user)


class RoomNameDeviceByName(AuthenticatedMixin, generics.ListAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        room_name = self.kwargs["name"]
        device_name = self.kwargs["device_name"]
        return Device.objects.filter(
            room__home__user=self.request.user,
            room__name=room_name,
            name=device_name,
        ).select_related("room")


class RoomAddDevice(AuthenticatedMixin, generics.CreateAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.filter(room__home__user=self.request.user)

    def perform_create(self, serializer):
        room = get_object_or_404(
            Room.objects.select_related("home"),
            home__user=self.request.user,
            name=self.kwargs["name"],
        )
        serializer.save(room=room)


class RoomTelemetry(AuthenticatedMixin, generics.ListAPIView):
    serializer_class = TelemetrySerializer

    def get_queryset(self):
        room_name = self.kwargs["name"]
        return Telemetry.objects.filter(
            device__room__home__user=self.request.user,
            device__room__name=room_name,
        ).select_related("device", "device__room")


class AlarmsList(AlarmList):
    pass
