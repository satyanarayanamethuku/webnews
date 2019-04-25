from .models import Aritcle,Reporter
from rest_framework import serializers

class AritcleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aritcle
        fields='__all__'
        depth=2 

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reporter
        fields='__all__'
        



