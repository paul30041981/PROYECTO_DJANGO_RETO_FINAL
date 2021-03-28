from rest_framework import serializers
from .models import Leccionunidad


class LeccionunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Leccionunidad
        fields = '__all__'
