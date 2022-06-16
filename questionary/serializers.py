from rest_framework import serializers
from .models import FeatureQuestion as FeatureQuestionModel, QualificationQuestion as QualificationQuestionModel, \
    Questionary as QuestionaryModel, User


class QualificationQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestionModel
        fields = ("id", "questionary", "question", "answer_variants", 'is_multiple')


class QualificationQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestionModel
        exclude = ("id",)


class FeatureQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureQuestionModel
        exclude = ("questionary", "feature_name", 'feature_description')


class FeatureQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureQuestionModel
        exclude = ("id",)


class QuestionarySerializer(serializers.ModelSerializer):
    qualification_questions = QualificationQuestionSerializer(many=True)
    feature_questions = FeatureQuestionSerializer(many=True)

    def create(self, validated_data):
        last_questionary_id = QuestionaryModel.objects.all().last().id

        qualification_questions = validated_data.pop('qualification_questions')
        feature_questions = validated_data.pop('feature_questions')
        questionary = QuestionaryModel.objects.create(**validated_data)

        for q_question in qualification_questions:
            QualificationQuestionModel.objects.create(questionary=last_questionary_id+1, **q_question)

        for f_question in feature_questions:
            FeatureQuestionModel.objects.create(questionary=last_questionary_id+1, **f_question)

        # print(good_request)

        return questionary

    class Meta:
        model = QuestionaryModel
        fields = ("name", "user", "qualification_questions", "feature_questions")
