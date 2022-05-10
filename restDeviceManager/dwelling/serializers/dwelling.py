from rest_framework import serializers
from ..models.dwelling import Dwelling

class DwellingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dwelling
        fields = '__all__'