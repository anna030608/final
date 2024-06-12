from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import api_views

urlpatterns = [
    path('fbv/questions/', api_views.questions_api_view),
    path('fbv/questions/<int:question_id>', api_views.question_api_view),
    path('fbv/answers/', api_views.answers_api_view),
    path('fbv/answers/<int:answer_id>', api_views.answer_api_view),
]
