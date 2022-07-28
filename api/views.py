from rest_framework.views import APIView
from questionary.models import Questionary as QuestionaryModel, \
    QualificationQuestion as QualificationQuestionModel, \
    FeatureQuestion as FeatureQuestionModel, Response as ResponseModel
from rest_framework.response import Response as ResponseJson
from api.serializers import QuestionarySerializer, QualificationQuestionSerializer, \
    QualificationQuestionCreateSerializer, FeatureQuestionSerializer, FeatureQuestionCreateSerializer, \
    QuestionaryListSerializer, ResponseSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView


class QualificationQuestionGet(APIView):
    def get(self, request, pk: int):
        qualification_question = QualificationQuestionModel.objects.get(id=pk)
        serializer = QualificationQuestionSerializer(qualification_question)

        return ResponseJson(serializer.data)


class QuestionaryList(ListAPIView):
    queryset = QuestionaryModel.objects.all()
    serializer_class = QuestionaryListSerializer


class Response(CreateAPIView):
    serializer_class = ResponseSerializer

    def get(self, request, pk: int):
        response = ResponseModel.objects.get(id=pk)
        serializer = ResponseSerializer(response)

        return ResponseJson(serializer.data)


class QualificationQuestionCreate(APIView):
    def post(self, request):
        serializer = QualificationQuestionCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        response = {
            "status": "200",
            "message": "Created successfully"
        }

        return ResponseJson(response)


class FeatureQuestionGet(APIView):
    def get(self, request, pk: int):
        feature_question = FeatureQuestionModel.objects.get(id=pk)
        serializer = FeatureQuestionSerializer(feature_question)

        return ResponseJson(serializer.data)


class FeatureQuestionList(APIView):
    def get(self, request):
        questions = FeatureQuestionModel.objects.all()
        serializer = FeatureQuestionSerializer(questions, many=True)

        return ResponseJson(serializer.data)


class FeatureQuestionCreate(APIView):
    def post(self, request):
        serializer = FeatureQuestionCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        response = {
            "status": "200",
            "message": "Created successfully"
        }

        return ResponseJson(response)


class Questionary(CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView):
    queryset = QuestionaryModel.objects.all()
    serializer_class = QuestionarySerializer

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return ResponseJson({"error": "Method put not allowed"})

        try:
            instance = QuestionaryModel.objects.get(pk=pk)
        except:
            return ResponseJson({"error": "Method put not allowed"})

        serializer = QuestionarySerializer(data=request.data, instance=instance)
        serializer.is_valid()
        serializer.save()

        return ResponseJson({"request": serializer.data})
