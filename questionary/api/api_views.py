from rest_framework.views import APIView
from questionary.models import Feedback, Questionary, QualificationQuestion, FeatureQuestion
from questionary.dto import FeatureQuestionBaseModel, QualificationQuestionsBaseModel, FeatureQuestionsBaseModel
from rest_framework.response import Response
from questionary.serializers import FeatureQuestionSerializer, QualificationQuestionSerializer, \
    QualificationQuestionCreateSerializer


class QualificationQuestionGet(APIView):
    def get(self, request, pk):
        qualification_question = QualificationQuestion.objects.get(id=pk)
        serializer = QualificationQuestionSerializer(qualification_question)

        return Response(serializer.data)


class QualificationQuestionList(APIView):
    def get(self, request):
        qualification_question = QualificationQuestion.objects.all()
        serializer = QualificationQuestionSerializer(qualification_question, many=True)

        serializer_in_json = QualificationQuestionsBaseModel(questions=serializer.data)

        parsed_json = serializer_in_json.dict()

        return Response(parsed_json)


class QualificationQuestionCreate(APIView):
    def post(self, request):
        serializer = QualificationQuestionCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response("success created")


class FeatureQuestionGet(APIView):
    def get(self, request, pk):
        feature_question = FeatureQuestion.objects.get(id=pk)
        serializer = FeatureQuestionSerializer(feature_question)

        return Response(serializer.data)


class FeatureQuestionList(APIView):
    def get(self, request):
        question = FeatureQuestion.objects.all()
        serializer = FeatureQuestionSerializer(question, many=True)

        serializer_in_json = FeatureQuestionsBaseModel(questions=serializer.data)

        parsed_data = serializer_in_json.dict()

        return Response(parsed_data)


class FeatureQuestionCreate(APIView):
    def post(self, request):
        serializer = FeatureQuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response("success created")