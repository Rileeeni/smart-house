from django.shortcuts import render
from rest_framework import generics
from .serializers import TelemetrySerializer
from .models import Telemetry
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class MySecureView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated)

class TelemetryAPIView(generics.ListAPIView):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer

from rest_framework import viewsets
from .models import Telemetry
from .serializers import TelemetrySerializer

class TelemetryViewSet(viewsets.ModelViewSet):
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
# Create your views here.
