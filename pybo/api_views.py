from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import AuthorWritePermission
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, Answer


def question_api_view(ModelViewSet):
    def get(se)



"""@api_view(['GET', 'POST'])
def questions_api_view(request: Request):
    if request.method == 'GET':
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = QuestionSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(author=request.user)
                return Response(data=serializer.data)"""


def question_api_view(ModelViewSet):

@api_view(['GET', 'PUT', 'DELETE'])
def question_api_view(request: Request, question_id: int):
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(data=serializer.data)
    else:
        # Authentication
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # Permission
        elif question.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            if request.method == 'PUT':
                serializer = QuestionSerializer(data=request.data)
                if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    serializer.save(author=request.user)
                    return Response(data=serializer.data, status=status.HTTP_200_OK)
            elif request.method == 'DELETE':
                question.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def answers_api_view(request: Request):
    if request.method == 'GET':
        queryset = Answer.objects.all()
        serializer = AnswerSerializer(queryset, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = AnswerSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(author=request.user)
                return Response(data=serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def answer_api_view(request: Request, answer_id: int):
    answer = get_object_or_404(Answer, id=answer_id)

    if request.method == 'GET':
        serializer = AnswerSerializer(answer)
        return Response(data=serializer.data)
    else:
        # Authentication
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # Permission
        elif answer.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            if request.method == 'PUT':
                serializer = AnswerSerializer(data=request.data)
                if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    serializer.save(author=request.user)
                    return Response(data=serializer.data, status=status.HTTP_200_OK)
            elif request.method == 'DELETE':
                answer.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
