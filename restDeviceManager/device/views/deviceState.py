from rest_framework.viewsets import ModelViewSet

from ..models.deviceState import DeviceState
from ..serializers.deviceState import DeviceStateSerializer

class DeviceStateView(ModelViewSet):
    queryset = DeviceState.objects.all()
    serializer_class = DeviceStateSerializer