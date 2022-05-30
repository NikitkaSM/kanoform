from rest_framework.views import APIView
from questionary.models import Feedback, Questionary as QuestionaryModel, \
    QualificationQuestion as QualificationQuestionModel, \
    FeatureQuestion as FeatureQuestionModel
from questionary.dto import FeatureQuestion as FeatureQuestionDto, \
    QualificationQuestion as QualificationQuestionDto, Questionary as QuestionaryCreateDto
from rest_framework.response import Response
from questionary.serializers import QuestionarySerializer, QualificationQuestionSerializer, \
    QualificationQuestionCreateSerializer, FeatureQuestionSerializer, FeatureQuestionCreateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView


class QualificationQuestionGet(APIView):
    def get(self, request, pk: int):
        qualification_question = QualificationQuestionModel.objects.get(id=pk)
        serializer = QualificationQuestionSerializer(qualification_question)

        return Response(serializer.data)


class QualificationQuestionList(APIView):
    def get(self, request):
        qualification_question = QualificationQuestionModel.objects.all()
        serializer = QualificationQuestionSerializer(qualification_question, many=True)

        serializer_in_json = QualificationQuestionDto(questions=serializer.data)

        parsed_json = serializer_in_json.dict()

        return Response(parsed_json)


class QualificationQuestionCreate(APIView):
    def post(self, request):
        serializer = QualificationQuestionCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        response = {
            "status": "200",
            "message": "Created successfully"
        }

        return Response(response)


class FeatureQuestionGet(APIView):
    def get(self, request, pk: int):
        feature_question = FeatureQuestionModel.objects.get(id=pk)
        serializer = FeatureQuestionSerializer(feature_question)

        return Response(serializer.data)


class FeatureQuestionList(APIView):
    def get(self, request):
        question = FeatureQuestionModel.objects.all()
        serializer = FeatureQuestionSerializer(question, many=True)

        serializer_in_json = QualificationQuestionDto(questions=serializer.data)

        parsed_data = serializer_in_json.dict()

        return Response(parsed_data)


class FeatureQuestionCreate(APIView):
    def post(self, request):
        serializer = FeatureQuestionCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        response = {
            "status": "200",
            "message": "Created successfully"
        }

        return Response(response)


class Questionary(CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView):
    queryset = QuestionaryModel.objects.all()
    serializer_class = QuestionarySerializer

    # def get(self, request):
    #     objects = QuestionaryModel.objects.all()
    #     serializer = QuestionarySerializer(objects, many=True)
    #
    #     return Response(serializer.data)
