from rest_framework import serializers
from .models.hub import Hub

class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = '__all__'

    # def update(self, instance:Hub, validated_data):
    #     devices = validated_data.pop('devices', None)
    #     instance = super().update(instance, validated_data)

    #     if devices is not None:
    #         for device in devices:
    #             instance.devices.add(device)
    #         instance.save()

    #     return instance