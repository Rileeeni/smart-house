from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Device, Home, Profile, Room, Scenarios, Telemetry
from .serializers import DeviceSerializer, RoomSerializer, ScenariosSerializer


class SmartHouseApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="owner", password="strong-password")
        self.other_user = User.objects.create_user(username="other", password="strong-password")

        self.profile = Profile.objects.create(username=self.user, email="owner@example.com")
        self.other_profile = Profile.objects.create(username=self.other_user, email="other@example.com")

        self.home = Home.objects.create(user=self.user, name="Main home")
        self.other_home = Home.objects.create(user=self.other_user, name="Other home")

        self.room = Room.objects.create(home=self.home, name="Hall")
        self.other_room = Room.objects.create(home=self.other_home, name="Guest room")

        self.device = Device.objects.create(
            room=self.room,
            name="Sensor",
            secret_key="secret-key-001",
        )
        self.other_device = Device.objects.create(
            room=self.other_room,
            name="Camera",
            secret_key="secret-key-002",
        )

        Telemetry.objects.create(device=self.device, temperature=22, humidity=40, motion=False, smoke=False)
        Telemetry.objects.create(device=self.device, temperature=23, humidity=41, motion=True, smoke=False)
        Telemetry.objects.create(
            device=self.other_device,
            temperature=18,
            humidity=55,
            motion=True,
            smoke=True,
        )

        self.client.force_authenticate(user=self.user)

    def test_room_serializer_rejects_blank_name(self):
        serializer = RoomSerializer(data={"name": "   ", "home": self.home.id})
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)

    def test_device_serializer_rejects_short_secret_key(self):
        serializer = DeviceSerializer(data={"name": "Lamp", "secret_key": "short"})
        self.assertFalse(serializer.is_valid())
        self.assertIn("secret_key", serializer.errors)

    def test_scenarios_serializer_requires_devices(self):
        serializer = ScenariosSerializer(
            data={"device": [], "scenario": {"action": "turn_on"}},
            context={"request": type("Request", (), {"user": self.user})()},
        )
        self.assertFalse(serializer.is_valid())
        self.assertIn("device", serializer.errors)

    def test_me_endpoint_returns_profile(self):
        response = self.client.get(reverse("me"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "owner")
        self.assertEqual(response.data["email"], "owner@example.com")

    def test_rooms_endpoint_shows_only_current_user_rooms(self):
        response = self.client.get(reverse("rooms"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Hall")

    def test_room_add_device_uses_room_from_url(self):
        response = self.client.post(
            reverse("room_add_device", kwargs={"name": self.room.name}),
            {"name": "Socket", "secret_key": "secret-key-003"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created = Device.objects.get(name="Socket")
        self.assertEqual(created.room, self.room)

    def test_room_telemetry_returns_only_room_data(self):
        response = self.client.get(reverse("telemetry", kwargs={"name": self.room.name}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertTrue(all(item["device"] == self.device.id for item in response.data))

    def test_alarm_endpoint_returns_only_triggered_items(self):
        response = self.client.get(reverse("alarms"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(response.data[0]["motion"] or response.data[0]["smoke"])

    def test_scenarios_create_assigns_current_user(self):
        response = self.client.post(
            reverse("scenarios_add"),
            {"device": [self.device.id], "scenario": {"action": "notify"}},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        scenario = Scenarios.objects.get(pk=response.data["id"])
        self.assertEqual(scenario.user, self.user)
        self.assertEqual(list(scenario.device.all()), [self.device])
