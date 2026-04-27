from django.contrib import admin

from .models import Profile, Telemetry, Scenarios,Device,Room,Home,Category

admin.site.register(Profile)
admin.site.register(Telemetry)
admin.site.register(Scenarios)
admin.site.register(Device)
admin.site.register(Room)
admin.site.register(Home)
admin.site.register(Category)
