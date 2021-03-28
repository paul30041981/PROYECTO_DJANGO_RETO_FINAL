from django.contrib import admin
from django.urls import path, include
from .views import HorariocursoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/horarioscursos', HorariocursoViewSet, basename='horarioscursos')

urlpatterns = [
]

urlpatterns += router.urls