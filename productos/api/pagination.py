from rest_framework.pagination import PageNumberPagination


class PaginacionProductos(PageNumberPagination):
    page_size = 2