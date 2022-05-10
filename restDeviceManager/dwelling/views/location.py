from rest_framework.viewsets import ModelViewSet

from ..models.location import Location
from ..serializers.location import LocationSerializer

class LocationView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer