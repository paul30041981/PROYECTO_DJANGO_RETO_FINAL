from django.contrib import admin
from django.urls import path, include
from .views import HorariocursoListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('v1/horarioscursos', HorariocursoViewSet, basename='horarioscursos')

urlpatterns = [
  path('v1/horarioscursos/', HorariocursoListView.as_view(), name='horarioscursos'),
]

urlpatterns += router.urls