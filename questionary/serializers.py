from rest_framework import serializers
from .models import FeatureQuestion, QualificationQuestion


class QualificationQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestion
        fields = ("id", "questionary", "question", "answer_variants", 'is_multiple')


class QualificationQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestion
        exclude = ("id",)


class FeatureQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureQuestion
        exclude = ("id",)