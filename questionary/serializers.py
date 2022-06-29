from rest_framework import serializers
from .models import FeatureQuestion as FeatureQuestionModel, QualificationQuestion as QualificationQuestionModel, \
    Questionary as QuestionaryModel


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

        qualification_questions = validated_data.pop('qualification_questions')
        feature_questions = validated_data.pop('feature_questions')
        questionary = QuestionaryModel.objects.create(user=user, **validated_data)

        for q_question in qualification_questions:
            QualificationQuestionModel.objects.create(questionary=questionary, **q_question)

        for f_question in feature_questions:
            FeatureQuestionModel.objects.create(questionary=questionary, **f_question)

        return questionary

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        feature_questions = validated_data['feature_questions']
        qualification_questions = validated_data["qualification_questions"]

        instance.feature_questions = []
        instance.qualification_questions = []

        for f_question in validated_data.get('feature_questions', None):
            instance.feature_questions.append(f_question)

        for q_question in validated_data.get('qualification_questions', None):
            instance.qualification_questions.append(q_question)

        instance.qualification_questions.set(validated_data["qualification_questions"])
        instance.feature_questions.set(validated_data["feature_questions"])

        instance.save()

        return instance

    class Meta:
        model = QuestionaryModel
        exclude = ("id",)
        depth = 1
