from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView


class UsersListAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_list = []
        for user in users:
            users_list.append({
                'id': user.pk,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username
            })
        return Response(users_list)
