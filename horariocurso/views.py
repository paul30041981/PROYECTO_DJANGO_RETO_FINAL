from django.shortcuts import render
from .models import Horariocurso
from .serializers import HorariocursoSerializer
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.


class HorariocursoViewSet(viewsets.ModelViewSet):
    queryset = Horariocurso.objects.all()
    serializer_class = HorariocursoSerializer
    # permission_classes = (permissions.IsAuthenticated, )