from rest_framework.viewsets import ModelViewSet

from ..models.device import Device
from ..serializers.device import DeviceSerializer

class DeviceView(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer