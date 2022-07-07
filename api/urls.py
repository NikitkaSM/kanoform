from django.urls import path
from api.views import FeatureQuestionGet, FeatureQuestionList, \
    QuestionaryList, QualificationQuestionGet, QualificationQuestionCreate, FeatureQuestionCreate, \
    Questionary

urlpatterns = [
    path("qualification-question/<int:pk>", QualificationQuestionGet.as_view()),
    path("qualification-question-create/", QualificationQuestionCreate.as_view()),

    path("feature-question/<int:pk>", FeatureQuestionGet.as_view()),
    path("feature-question-list/", FeatureQuestionList.as_view()),
    path("feature-question-create/", FeatureQuestionCreate.as_view()),

    path("questionary/", Questionary.as_view()),
    path("questionary-list/", QuestionaryList.as_view()),
    path("questionary/<int:pk>", Questionary.as_view()),
]
