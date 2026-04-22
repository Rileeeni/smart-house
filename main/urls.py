from django.urls import path
from .views import Me,AlarmList,ScenariosList,ScenariosAdd,RoomAdd,RoomIdDeviceByName,RoomAddDevice,ScenariosById,ListRoom,DeviceList,RoomTelemetry
urlpatterns = [
   # path('/api/v1/auth/login',),
   #  path('/api/v1/auth/regis'),
    path('/api/v1/me',Me.as_view(),name='me'),
    path("/api/v1/me/rooms",ListRoom.as_view(),name='rooms'),
    # path('/api/v1/me/room/{name}/',),
    path('/api/v1/me/alarms/',AlarmList.as_view(),name='alarms'),
    path('/api/v1/me/room/{name}/telemetry/',RoomTelemetry.as_view(),name='telemetry'),
    path('/api/v1/me/scenarios',ScenariosList.as_view(),name='scenarios'),
    path('/api/v1/me/scenarios/add',ScenariosAdd.as_view(),name='scenarios_add'),
    path('/api/v1/me/scenarios/{id}/',ScenariosById.as_view(),name='scenarios_id'),
    path('/api/v1/me/room/add/',RoomAdd.as_view(),name='room_add'),
    path("/api/v1/me/rom/devices",DeviceList.as_view(),name='device_list'),
    path('/api/v1/me/room/{name}/device/{name}/',RoomIdDeviceByName.as_view(),name='room_device'),
    path('/api/v1/me/room/{name}/device/add',RoomAddDevice.as_view(),name='room_add_device'),
]
