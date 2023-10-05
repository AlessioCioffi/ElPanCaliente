from .serializer import ProductoSerializer
from rest_framework.viewsets import ModelViewSet

from ..models import Producto

from .permissions import PermisoUserAutenticado
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import PaginacionProductos

class ProductoApiViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = [PermisoUserAutenticado]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre']
    pagination_class = PaginacionProductos

"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductoApiView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoApiDetailView(APIView):

    def get(self,pk):
        producto = self.get_object(pk)
        if producto is not None:
            serializer = ProductoSerializer(producto)
            return Response(serializer.data)
        return Response({"detail": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        producto = self.get_object(pk)
        if producto is not None:
            serializer = ProductoSerializer(producto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,pk):
        producto = self.get_object(pk)
        if producto is not None:
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)"""

