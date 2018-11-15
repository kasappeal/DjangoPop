from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ads.models import Ad
from ads.serializers import AdListSerializer, AdSerializer


class AdListAPIView(ListCreateAPIView):

    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return AdListSerializer if self.request.method == 'GET' else AdSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
