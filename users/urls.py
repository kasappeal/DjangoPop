from django.urls import path

from users.api import UsersListAPIView, UserDetailAPIView
from users.views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),

    # API
    path('api/1.0/users/', UsersListAPIView.as_view(), name='users_list_api'),
    path('api/1.0/users/<int:pk>', UserDetailAPIView.as_view(), name='user_detail_api')
]
