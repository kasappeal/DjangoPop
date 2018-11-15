from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.permissions import AdPermission
from ads.serializers import AdListSerializer, AdSerializer


class AdViewSet(ModelViewSet):

    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, AdPermission]
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'owner__first_name', 'owner__last_name']
    ordering = ['id', 'price', 'status', 'name', 'pub_date', 'last_modification']
    filter_fields = ['status', 'owner', 'price']

    def get_queryset(self):
        return self.queryset if self.request.user.is_authenticated else self.queryset.filter(status=Ad.PUBLISHED)

    def get_serializer_class(self):
        return AdListSerializer if self.action == 'list' else AdSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False)
    def me(self, request):
        ads = Ad.objects.filter(owner=request.user)
        serializer = AdListSerializer(ads, many=True)
        return Response(serializer.data)
