from django.shortcuts import render
from .models import Interesado
from .serializers import InteresadoSerializer
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.


class InteresadoViewSet(viewsets.ModelViewSet):
    queryset = Interesado.objects.all()
    serializer_class = InteresadoSerializer
    # permission_classes = (permissions.IsAuthenticated, )