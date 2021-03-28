from django.contrib import admin
from django.urls import path, include
from .views import UnidadcursoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/unidadescursos', UnidadcursoViewSet, basename='unidadescursos')

urlpatterns = [
]

urlpatterns += router.urls