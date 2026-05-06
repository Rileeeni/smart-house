from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
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
    permission_classes = [IsAuthenticated]


class TelemetryAPIView(generics.ListAPIView):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]



class TelemetryViewSet(viewsets.ModelViewSet):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]



class Me(APIView):
    """Профиль"""
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

    def get(self, request):
        serializer =ProfileSerializers(request.user.profile)
        return Response(serializer.data)



class ListRoom(generics.ListAPIView):
    """Лист комнат"""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]



class AlarmList(generics.ListAPIView):
    """Лист Тревог"""
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]



class ScenariosList(generics.ListAPIView):
    """Лист сценариев"""
    queryset = Scenarios.objects.all()
    serializer_class = ScenariosSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]



class ScenariosAdd(CreateAPIView):
    """Добавить сценарий"""
    queryset = Scenarios.objects.all()
    serializer_class = ScenariosSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]



class ScenariosById(RetrieveUpdateDestroyAPIView):
    """Сценарий по айди"""
    queryset = Scenarios.objects.all()
    serializer_class = ScenariosSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]



class DeviceList(generics.ListAPIView):
    """Лист Девайсов"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]



class RoomAdd(CreateAPIView):
    """Добавить комнату"""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]



class RoomNameDeviceByName(ListAPIView):
    """Опред.девайс в опред. комнате """
    queryset = Room.objects.all()
    serializer_class = DeviceSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_name = self.kwargs['room_name']
        device_name = self.kwargs['device_name']
        return Device.objects.filter(room_name=room_name, name=device_name)



class RoomAddDevice(CreateAPIView):
    """Добавить девайс в комнату"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        room_name = self.kwargs['room_name']
        serializer.save(room_name=room_name)




class RoomTelemetry(generics.ListAPIView):
    """Телеметрия опред.комнаты"""
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_name = self.kwargs['room_name']
        device_name = self.kwargs['device_name']
        queryset = Telemetry.objects.all()

        if room_name:
            queryset = queryset.filter(room_name=room_name)
        if device_name:
            queryset = queryset.filter(device_name=device_name)

        return queryset

    def get_queryset(self):
        room_name = self.kwargs['room_name']
        return Telemetry.objects.filter(room_name=room_name)



class AlarmsList(generics.ListAPIView):
    """Лист тревог"""
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]

