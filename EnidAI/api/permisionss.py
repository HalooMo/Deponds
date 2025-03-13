from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsOwnOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.methods in permissions.SAFE_METHODS:
            return True
        return request.user == obj.auth_licensed or request.user == obj.auth_depond

