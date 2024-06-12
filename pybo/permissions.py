from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated

from pybo.models import Question, Answer


class AuthorWritePermission(IsAuthenticated):
    pass
