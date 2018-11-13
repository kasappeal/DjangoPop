from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View

import json


class UsersListAPIView(View):

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
        users_json = json.dumps(users_list)
        return HttpResponse(users_json, content_type='application/json')
