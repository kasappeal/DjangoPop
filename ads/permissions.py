from rest_framework.permissions import BasePermission


class AdPermission(BasePermission):

    def has_permission(self, request, view):
        # define si el usuario autenticado puede realizar la acción
        return request.user.is_authenticated or request.method == 'GET'

    def has_object_permission(self, request, view, obj):
        # define si el usuario autenticado puede realizar la acción sobre el objeto obj
        return request.method == 'GET' or obj.owner == request.user or request.user.is_superuser
