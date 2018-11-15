from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ads.models import Ad
from ads.serializers import AdListSerializer, AdSerializer


class AdListAPIView(ListCreateAPIView):

    queryset = Ad.objects.all()

    def get_serializer_class(self):
        return AdListSerializer if self.request.method == 'GET' else AdSerializer


class AdDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
