from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics, permissions

from pybo import models
from pybo.models import Question, Answer


class AuthorWritePermission(IsAuthenticated):
    # pass
    def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user