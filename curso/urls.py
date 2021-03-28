from django.contrib import admin
from django.urls import path, include
from .views import CursoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/cursos', CursoViewSet, basename='cursos')

urlpatterns = [
]

urlpatterns += router.urls