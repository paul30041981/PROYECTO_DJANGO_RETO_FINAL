from django.contrib import admin
from django.urls import path, include
from .views import ImagenescursoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/imagenescursos', ImagenescursoViewSet, basename='imagenescursos')

urlpatterns = [
]

urlpatterns += router.urls