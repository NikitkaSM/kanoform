from rest_framework.views import APIView
from questionary.models import Questionary as QuestionaryModel, \
    QualificationQuestion as QualificationQuestionModel, \
    FeatureQuestion as FeatureQuestionModel
from api.dto import QualificationQuestion as QualificationQuestionDto
from rest_framework.response import Response
from api.serializers import QuestionarySerializer, QualificationQuestionSerializer, \
    QualificationQuestionCreateSerializer, FeatureQuestionSerializer, FeatureQuestionCreateSerializer, \
    QuestionaryListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView


class QualificationQuestionGet(APIView):
    def get(self, request, pk: int):
        qualification_question = QualificationQuestionModel.objects.get(id=pk)
        serializer = QualificationQuestionSerializer(qualification_question)

        return Response(serializer.data)


class QuestionaryList(ListAPIView):
    queryset = QuestionaryModel.objects.all()
    serializer_class = QuestionaryListSerializer


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

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method put not allowed"})

        try:
            instance = QuestionaryModel.objects.get(pk=pk)
        except:
            return Response({"error": "Method put not allowed"})

        serializer = QuestionarySerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()
        return Response({"request": serializer.data})
