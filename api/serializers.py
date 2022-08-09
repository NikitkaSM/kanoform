from rest_framework import serializers
from questionary.models import FeatureQuestion as FeatureQuestionModel, \
    QualificationQuestion as QualificationQuestionModel, Questionary as QuestionaryModel, \
    QualificationResponse as QualificationResponseModel, FeatureResponse as FeatureResponseModel, \
    Response as ResponseModel, Feedback as FeedbackModel
from django.contrib.auth.models import User
import hashlib
import os


class QualificationQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestionModel
        fields = ("id", "question", "answer_variants", 'is_multiple')


class QualificationQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestionModel
        exclude = ("id",)


class FeatureQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureQuestionModel
        fields = ("id", "feature_name", 'feature_description')


class FeatureQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureQuestionModel
        exclude = ("id",)


class QuestionarySerializer(serializers.ModelSerializer):
    qualification_questions = QualificationQuestionSerializer(many=True)
    feature_questions = FeatureQuestionSerializer(many=True)

    def create(self, validated_data):
        user = self.context["request"].user

        qualification_questions = validated_data.pop('qualification_questions')
        feature_questions = validated_data.pop('feature_questions')
        questionary = QuestionaryModel.objects.create(user=user, **validated_data)

        for q_question in qualification_questions:
            QualificationQuestionModel.objects.create(questionary=questionary, **q_question)

        for f_question in feature_questions:
            FeatureQuestionModel.objects.create(questionary=questionary, **f_question)

        return questionary

    def update(self, instance, validated_data):
        feature_questions = validated_data.pop('feature_questions')
        qualification_questions = validated_data.pop("qualification_questions")
        instance.name = validated_data["name"]

        questionary_id = instance.id
        questionary = QuestionaryModel.objects.get(pk=questionary_id)

        QualificationQuestionModel.objects.filter(questionary=questionary).delete()
        FeatureQuestionModel.objects.filter(questionary=questionary).delete()

        for f_question in feature_questions:
            FeatureQuestionModel.objects.create(questionary=questionary, **f_question)

        for q_question in qualification_questions:
            QualificationQuestionModel.objects.create(questionary=questionary, **q_question)

        instance.save()

        return instance

    class Meta:
        model = QuestionaryModel
        exclude = ("id",)
        depth = 1


class QuestionaryListSerializer(serializers.ModelSerializer):
    qualification_questions = QualificationQuestionSerializer(many=True)
    feature_questions = FeatureQuestionSerializer(many=True)

    class Meta:
        model = QuestionaryModel
        fields = ("id", "name", "user", "qualification_questions", "feature_questions", "created_time")
        depth = 1


class QualificationResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationResponseModel
        fields = ("id", "qualification_question", "answer")


class FeatureResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureResponseModel
        fields = ("id", "answer_1", "answer_2", "answer_3", "feature_question")


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = ("id", "first_name", "last_name", "email", "messenger", "phone_number")


class ResponseSerializer(serializers.ModelSerializer):
    qualification_response = QualificationResponseSerializer(many=True)
    feature_response = FeatureResponseSerializer(many=True)
    feedback = FeedbackSerializer

    def create(self, validated_data):
        context = self.context['request'].data
        feedback = context.get("feedback")
        questionary = context.get("questionary").get("id")
        questionary_instance = QuestionaryModel.objects.get(id=questionary)
        qualification_response = validated_data.pop("qualification_response")
        feature_response = validated_data.pop("feature_response")
        response = ResponseModel.objects.create(questionary=questionary_instance)
        FeedbackModel.objects.create(response=response, **feedback)

        for q_response in qualification_response:
            QualificationResponseModel.objects.create(response=response, **q_response)

        for f_response in feature_response:
            FeatureResponseModel.objects.create(response=response, **f_response)

        return response

    class Meta:
        model = ResponseModel
        fields = ("id", "feedback", "questionary", "qualification_response", 'feature_response')
        depth = 2


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        context: dict = self.context['request'].data
        user = User.objects.create(username=context["username"], first_name=context["first_name"])
        user.set_password(context["password"])
        user.save()

        return user

    class Meta:
        model = User
        fields = ("first_name", "username", "password")
