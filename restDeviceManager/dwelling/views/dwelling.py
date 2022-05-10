from rest_framework.viewsets import ModelViewSet

from ..models.dwelling import Dwelling
from ..serializers.dwelling import DwellingSerializer

class DwellingView(ModelViewSet):
    queryset = Dwelling.objects.all()
    serializer_class = DwellingSerializer

