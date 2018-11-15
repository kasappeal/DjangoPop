from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ads.models import Ad
from ads.permissions import AdPermission
from ads.serializers import AdListSerializer, AdSerializer


class AdListAPIView(ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Ad.objects.all() if self.request.user.is_authenticated else Ad.objects.filter(status=Ad.PUBLISHED)

    def get_serializer_class(self):
        return AdListSerializer if self.request.method == 'GET' else AdSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AdPermission]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
