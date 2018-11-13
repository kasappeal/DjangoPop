from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ads.models import Ad
from ads.serializers import AdListSerializer, AdSerializer


class AdListAPIView(APIView):

    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdListSerializer(ads, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
