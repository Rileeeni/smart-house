from django.urls import path

urlpatterns = [
   path('/api/v1/auth/login',),
    path('/api/v1/auth/regis'),
    path('/api/v1/me',),
    path('/api/v1/me/room/{name}/',),
    path('/api/v1/me/alarms/',),
    path('/api/v1/me/room/{name}/telemetry/',),
    path('/api/v1/me/scenarios',),
    path('/api/v1/me/scenarios/add',),
    path('/api/v1/me/scenarios/{id}/',),
    path('/api/v1/me/room/add/',),
    path('/api/v1/me/room/{name}/device/{name}/',),
    path('api/v1/me/room/{name}/device/add',),
]
