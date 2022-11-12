from rest_framework import serializers
from .models import Details,Brokers

class DetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model =Details
        fields ="__all__"

class BrokersSerialiser(serializers.ModelSerializer):
    class Meta:
        model =Brokers
        fields ="__all__"