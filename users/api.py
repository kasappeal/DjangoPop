from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer


class UsersListAPIView(APIView):

    permission_classes = [UserPermission]

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailAPIView(APIView):

    permission_classes = [UserPermission]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)  # devuelve una respuesta 400 BAD REQUEST con los errores de validación
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
