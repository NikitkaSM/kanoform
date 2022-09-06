from rest_framework.views import APIView
from questionary.models import Questionary as QuestionaryModel, \
    QualificationQuestion as QualificationQuestionModel, \
    FeatureQuestion as FeatureQuestionModel, Response as ResponseModel, FeatureResponse as FeatureResponseModel
from rest_framework.response import Response as ResponseJson
from api.serializers import QuestionarySerializer, QualificationQuestionSerializer, \
    QualificationQuestionCreateSerializer, FeatureQuestionSerializer, FeatureQuestionCreateSerializer, \
    QuestionaryListSerializer, ResponseSerializer, RegisterSerializer, FeatureAnswerVariantsSerializer, \
    FeatureResponseSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from django.contrib.auth.models import User as UserModel
from json import loads, dumps
from api.categories import categories

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


class Register(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer


# class Login(CreateAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = LoginSerializer  недоделанное апи логина


class Analytics(APIView):
    def get(self, request, pk):
        if request.method != "GET":
            return ResponseJson({"Bad Request": f"Метод {request.method} не разрешен"})
        
        results = {
                "Привлекательная": [],
                "Обязательная": [],
                "Одномерная": [],
                "Неважная": [],
                "Нежелательная": []
        }

        response = ResponseModel.objects.filter(questionary_id=pk)
        serializer = ResponseSerializer(response, many=True)  

        serialized_response = loads(dumps(serializer.data))

        for s_response in serialized_response:
            answer = {}

            for f_answer in s_response["feature_response"]:
                feature_name = FeatureQuestionModel.objects.get(pk=f_answer["feature_question"])
                serializer = FeatureQuestionSerializer(feature_name)
                
                feature_category = categories[f"{ f_answer['answer_1'] }+{ f_answer['answer_2'] }"]

                feature_answer = {
                        "name": serializer.data['feature_name'],
                        "implemented_score": f_answer["answer_1"],
                        "missing_score": f_answer["answer_2"],
                        "importance_score": f_answer["answer_3"]
                    }
                answer["feature"] = feature_answer

            for q_answer in s_response["qualification_response"]:
                question = QualificationQuestionModel.objects.get(pk=q_answer["qualification_question"])
                serializer = QualificationQuestionSerializer(question)
                
                qualification_answer = {
                        "question": serializer.data,
                        "answer": q_answer["answer"]
                    }
                answer["qualification"] = qualification_answer

            results[feature_category].append(answer)

        return ResponseJson(results)
