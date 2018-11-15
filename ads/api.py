from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.permissions import AdPermission
from ads.serializers import AdListSerializer, AdSerializer


class AdViewSet(ModelViewSet):

    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, AdPermission]

    def get_queryset(self):
        return self.queryset if self.request.user.is_authenticated else self.queryset.filter(status=Ad.PUBLISHED)

    def get_serializer_class(self):
        return AdListSerializer if self.action == 'list' else AdSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
