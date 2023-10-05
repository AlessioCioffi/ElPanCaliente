from rest_framework.routers import DefaultRouter
from .views import ProductoApiViewSet

productos_router = DefaultRouter()
productos_router.register(basename='productos', prefix='productos', viewset=ProductoApiViewSet)

"""
from django.urls import path
from .views import ProductoApiView, ProductoApiDetailView

urlpatterns = [
    path('productos/', ProductoApiView.as_view()),
    path('productos/<int:pk>/', ProductoApiDetailView.as_view()),
]
"""