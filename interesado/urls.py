from django.contrib import admin
from django.urls import path, include
from .views import InteresadoViewSet, InteresadoCreateAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('v1/interesados', InteresadoViewSet, basename='interesados')

urlpatterns = [
  path('v1/create/', InteresadoCreateAPI.as_view(), name='create'),
]

urlpatterns += router.urls