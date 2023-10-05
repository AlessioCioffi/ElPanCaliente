from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Producto


class ProductoCRUDTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/productos/"
        self.producto_data = {
            "nombre": "Pan",
            "descripcion": "Pane di campagana",
            "precio": 10.0,
            "stock": 100,
        }
        self.producto = Producto.objects.create(**self.producto_data)

    def test_creacion_de_producto(self):
        response = self.client.post(self.url, self.producto_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_obtener_detalle_de_producto(self):
        response = self.client.get(f"{self.url}{self.producto.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizacion_de_producto(self):
        updated_data = {
            "nombre": "Pan actualizado",
            "descripcion": "Pane di campagna actualizada",
            "precio": 15.0,
            "stock": 200,
        }
        response = self.client.put(f"{self.url}{self.producto.id}/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.nombre, "Pan actualizado")

    def test_eliminar_producto(self):
        response = self.client.delete(f"{self.url}{self.producto.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Producto.DoesNotExist):
            self.producto.refresh_from_db()


