from rest_framework import serializers
from .models import Unidadcurso


class UnidadcursoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Unidadcurso
        fields = '__all__'
