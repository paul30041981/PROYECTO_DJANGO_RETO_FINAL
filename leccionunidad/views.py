from django.shortcuts import render
from .models import Leccionunidad
from .serializers import LeccionunidadSerializer
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.


class LeccionunidadViewSet(viewsets.ModelViewSet):
    queryset = Leccionunidad.objects.all()
    serializer_class = LeccionunidadSerializer
    # permission_classes = (permissions.IsAuthenticated, )