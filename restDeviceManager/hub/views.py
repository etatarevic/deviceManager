from rest_framework.viewsets import ModelViewSet

from .models.hub import Hub
from .serializer import HubSerializer

class HubView(ModelViewSet):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer