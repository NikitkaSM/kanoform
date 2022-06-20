from django.http import HttpResponse
from rest_framework import serializers
from .models import FeatureQuestion as FeatureQuestionModel, QualificationQuestion as QualificationQuestionModel, \
    Questionary as QuestionaryModel
import json


class QualificationQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestionModel
        fields = ("question", "answer_variants", 'is_multiple')


class QualificationQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestionModel
        exclude = ("id",)


class FeatureQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureQuestionModel
        fields = ("feature_name", 'feature_description')


class FeatureQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureQuestionModel
        exclude = ("id",)


class QuestionarySerializer(serializers.ModelSerializer):
    qualification_questions = QualificationQuestionSerializer(many=True)
    feature_questions = FeatureQuestionSerializer(many=True)

    def create(self, validated_data):
        user = self.context["request"].user

        if not user:
            return HttpResponse("landing/")

        qualification_questions = validated_data.pop('qualification_questions')
        feature_questions = validated_data.pop('feature_questions')
        questionary = QuestionaryModel.objects.create(user=user, **validated_data)

        for q_question in qualification_questions:
            QualificationQuestionModel.objects.create(questionary=questionary, **q_question)

        for f_question in feature_questions:
            FeatureQuestionModel.objects.create(questionary=questionary, **f_question)

        return questionary

    def update(self, instance, validated_data):
        feature_questions = validated_data.pop("feature_questions")
        qualification_questions = validated_data.pop("qualification_questions")

        instance.name = validated_data.get("name", instance.name)

        for f_question in feature_questions:
            instance.feature_questions.feature_name = f_question.get(
                "feature_name",
                instance.feature_questions.feature_name)
            instance.feature_questions.feature_description = f_question.get(
                "feature_description",
                instance.feature_questions.feature_description)

        for q_question in qualification_questions:
            q_question['question'] = q_question.get("question", q_question['question'])
            q_question['is_multiple'] = q_question.get("is_multiple", q_question['is_multiple'])
            q_question['answer_variants'] = q_question.get("answer_variants", q_question['answer_variants'])

        instance.save()

        return instance

    class Meta:
        model = QuestionaryModel
        exclude = ("id",)
