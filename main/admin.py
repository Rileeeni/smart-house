from django.contrib import admin

from .models import Profile, Telemetry, Scenarios

admin.site.register(Profile)
admin.site.register(Telemetry)
admin.site.register(Scenarios)