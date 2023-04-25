from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.clientes.views import ClientesViewSet

router = DefaultRouter()
router.register(r'clientes', ClientesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

