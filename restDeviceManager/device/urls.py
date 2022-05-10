from django.urls import path
from .views import device, deviceState

urlpatterns = [
    path('', device.DeviceView.as_view(
            {
                "get":"list",
                "post":"create",
            }
        )),
    path('<slug:pk>/', device.DeviceView.as_view(
            {
                "get":"retrieve",
                "patch":"partial_update",
                "put":"update",
                "delete":"destroy",
            }
        )),
    path('device-state/', deviceState.DeviceStateView.as_view(
            {
                "get":"list",
                "post":"create",
            }
    )),
    path('device-state/<slug:pk>/', deviceState.DeviceStateView.as_view(
            {
                "get":"retrieve",
                "patch":"partial_update",
                "put":"update",
                "delete":"destroy",
            }
    )),
]