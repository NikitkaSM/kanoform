from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Questionary as QuestionaryModel, FeatureQuestion as FeatureQuestionModel, \
    QualificationQuestion as QualificationQuestionModel
from api.serializers import QuestionarySerializer
from json import loads, dumps
from django.contrib.auth.models import User


def questionary_fill_in(request, pk):
    queryset = QuestionaryModel.objects.get(id=pk).__dict__
    feature_questions_queryset = FeatureQuestionModel.objects.filter(questionary_id=queryset.get("id"))
    qualification_questions_queryset = QualificationQuestionModel.objects.filter(questionary_id=queryset.get("id"))
    feature_questions = []
    qualification_questions = []

    for f_question in list(feature_questions_queryset):
        feature_questions.append(f_question.__dict__)

    for q_question in list(qualification_questions_queryset):
        qualification_questions.append(q_question.__dict__)

    queryset["feature_questions"] = feature_questions
    queryset["qualification_questions"] = qualification_questions

    serializer = QuestionarySerializer(data=queryset)

    if serializer.is_valid():
        questionary = serializer.data
        author = User.objects.get(id=queryset.get("user_id"))

        context = {
            "name": questionary["name"],
            "qualification_questions": loads(dumps(questionary.get("qualification_questions"))),
            "feature_questions": loads(dumps(questionary.get("feature_questions"))),
            "author": author,
            "questionary_id": pk,
        }

        return render(request, "questionary/questionary-fill-in.html", context)

    return HttpResponse("not ok")


def handler404(request, exception):
    return render(request, "errorHandlers/404.html")


def handler500(request, *args, **argv):
    return render(request, 'errorHandlers/500.html', status=500)


def questionary_success_created(request):
    return render(request, "questionary/questionary_success_create.html")


def questionary_list(request):
    user = request.user

    if user.is_anonymous or not user.is_staff or not user.is_authenticated:
        raise Http404

    return render(request, 'questionary/questionary-list.html')


def questionary_creating(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        raise Http404

    return render(request, "questionary/questionary-creating.html")
