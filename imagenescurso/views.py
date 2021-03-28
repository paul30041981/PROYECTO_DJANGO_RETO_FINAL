from django.shortcuts import render
from .models import Imagenescurso
from .serializers import ImagenescursoSerializer
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.


class ImagenescursoViewSet(viewsets.ModelViewSet):
    queryset = Imagenescurso.objects.all()
    serializer_class = ImagenescursoSerializer
    # permission_classes = (permissions.IsAuthenticated, )