from django.shortcuts import render
from .models import Unidadcurso
from .serializers import UnidadcursoSerializer
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.


class UnidadcursoViewSet(viewsets.ModelViewSet):
    queryset = Unidadcurso.objects.all()
    serializer_class = UnidadcursoSerializer
    # permission_classes = (permissions.IsAuthenticated, )