"""Docstring"""
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'items', viewset=views.ItemViewSet)
router.register(r'orders', viewset=views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
