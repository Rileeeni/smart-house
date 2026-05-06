from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models import ManyToManyField
from rest_framework.exceptions import ValidationError





class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    password = models.CharField(max_length=100,validators=[
    MinValueValidator(8)
    ])
    def clean(self):
        if not self.email.strip():
            raise ValidationError("email не может быть пустым")
        if not self.password.strip():
            raise ValueError("password не может быть пустым")

class Home (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,validators=[
        MinValueValidator(4)
    ])
    def clean(self):
        if not self.name.strip():
            raise ValidationError("Название дома не может быть пустым")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],
                                    name='unique_name_review')
        ]

class Room(models.Model):
    home = models.ForeignKey("Home", on_delete=models.CASCADE)
    name = models.CharField(max_length=100,validators=[
        MinValueValidator(4)
    ])

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Название комнаты не может быть пустым")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],
                                    name='unique_room_name_review')
        ]


class Device(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    secret_key = models.CharField(max_length=255,validators=[
        MinValueValidator(12)
    ])
    name = models.CharField(max_length=100,validators=[
        MinValueValidator(4)
    ])
    def clean(self):
        if not self.name.strip():
            raise ValidationError("Название комнаты не может быть пустым")
        if not self.secret_key.strip():
            raise ValidationError("secret_key не может быть пустым")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],
                                    name='unique_device_review')
        ]


class Telemetry(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    temperature = models.FloatField(validators=[
    MinValueValidator(-50, message="Температура не может быть ниже -10"),
    MaxValueValidator(60, message="Температура не может быть выше 40"),
    ]
    )
    humidity = models.FloatField(validators=[
    MinValueValidator(0, message="Влажность должна быть в диапазоне от 0 до 100"),
    MaxValueValidator(100, message="Влажность должна быть в диапазоне от 0 до 100"),
    ]
    )
    motion = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100,validators=[
        MinValueValidator(4)
    ])
    def __str__(self):
        return self.name
    def clean(self):
        if not self.name.strip():
            raise ValidationError("Название дома не может быть пустым")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],
                                    name='unique_category_review')
        ]

class Scenarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = ManyToManyField(Device)
    scenario = models.JSONField(validators=[
        FileExtensionValidator(["json"])
    ])
    def clean(self):
        if not self.scenario.strip():
            raise ValidationError("Сценарий не может быть пустым")
        if not self.device.strip():
            raise ValidationError("Список девайсов не может быть пуст")





