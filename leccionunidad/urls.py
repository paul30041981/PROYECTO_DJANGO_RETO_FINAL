from django.contrib import admin
from django.urls import path, include
from .views import LeccionunidadViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/leccionesunidades', LeccionunidadViewSet, basename='leccionesunidades')

urlpatterns = [
]

urlpatterns += router.urls