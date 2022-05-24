from rest_framework import serializers
from .models import FeatureQuestion as FeatureQuestionModel, QualificationQuestion as QualificationQuestionModel, \
    Questionary as QuestionaryModel


class Questionary(serializers.ModelSerializer):
    class Meta:
        model = QuestionaryModel
        fields = ("name", "user")


class QualificationQuestion(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestionModel
        fields = ("id", "questionary", "question", "answer_variants", 'is_multiple')


class QualificationQuestionCreate(serializers.ModelSerializer):
    class Meta:
        model = QualificationQuestion
        exclude = ("id",)


class FeatureQuestion(serializers.ModelSerializer):
    class Meta:
        model = FeatureQuestionModel
        exclude = ("questionary", "feature_name", 'feature_description')


class FeatureQuestionCreate(serializers.ModelSerializer):
    class Meta:
        model = FeatureQuestionModel
        exclude = ("id",)


class QuestionaryCreate(serializers.Serializer):
    qualification_question = QualificationQuestion()
    feature_question = FeatureQuestion(many=True)
    questionary = Questionary(many=True)

    def create(self, validated_data):
        # questionary = QuestionaryModel.objects.update_or_create(
        #     user=validated_data.get("user"),
        #     name=validated_data.get('name')
        # )
        # qualification_question = QualificationQuestionModel.objects.update_or_create(
        #     questionary=
        # )
        return validated_data