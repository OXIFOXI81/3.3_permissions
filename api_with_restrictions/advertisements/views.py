from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import AdvertisementFilter
from .models import Advertisement
from .permissions import IsOwner
from .serializers import  AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == 'create':
            return [IsAuthenticated()]
        if self.action in ['destroy', 'update', 'partial_update']:
            return [IsAuthenticated(), IsOwner()]
        return []

# 287061478fc1590526312de3bf3caf01e41cb5e2
#     def get_permissions(self):
#         """Получение прав для действий."""
#         if self.action in ["create", "update", "partial_update"]:
#             return [IsAuthenticated()]
#         return []
