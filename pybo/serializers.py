from django.utils import timezone
from rest_framework import serializers
from .models import Question
from .models import Answer

"""class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('id', 'title', 'content', 'owner')"""

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        read_only_fields = ('author', 'create_date', 'modify_date')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        read_only_fields = ('author', 'create_date', 'modify_date')
