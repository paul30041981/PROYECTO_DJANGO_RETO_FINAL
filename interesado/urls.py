from django.contrib import admin
from django.urls import path, include
from .views import InteresadoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/interesados', InteresadoViewSet, basename='interesados')

urlpatterns = [
]

urlpatterns += router.urls