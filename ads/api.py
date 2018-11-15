from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from ads.models import Ad
from ads.serializers import AdListSerializer, AdSerializer


class AdListAPIView(ListCreateAPIView):

    queryset = Ad.objects.all()

    def get_serializer_class(self):
        return AdListSerializer if self.request.method == 'GET' else AdSerializer


class AdDetailAPIView(APIView):

    def get(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        serializer = AdSerializer(ad)
        return Response(serializer.data)

    def put(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        serializer = AdSerializer(ad, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
