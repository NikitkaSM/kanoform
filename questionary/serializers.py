from rest_framework import serializers
from .models import FeatureQuestion as FeatureQuestionModel, QualificationQuestion as QualificationQuestionModel, \
    Questionary as QuestionaryModel


class QuestionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionaryModel
        fields = ("name", "user")


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


class QuestionaryCreateSerializer(serializers.ModelSerializer):
    qualification_question = QualificationQuestionSerializer()
    feature_question = FeatureQuestionSerializer(many=True)
    questionary = QuestionarySerializer(many=True)

    class Meta:
        model = QuestionaryModel
        fields = ("user", "name")

    def create(self, validated_data):
        qualification_questions = validated_data.pop("qualification_question")
        feature_questions = validated_data.pop("feature_question")
        questionary = QuestionaryModel.objects.create(**validated_data)

        for qualification_question in qualification_questions:
            QualificationQuestionModel.objects.create(**qualification_question)

        for feature_question in feature_questions:
            FeatureQuestionModel.objects.create(**feature_question)

        return questionary
