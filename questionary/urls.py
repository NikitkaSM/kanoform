from django.urls import path
from questionary.api.views import FeatureQuestionGet, FeatureQuestionList, \
    QualificationQuestionList, QualificationQuestionGet, QualificationQuestionCreate, FeatureQuestionCreate, \
    QuestionaryCreate
from questionary.html.views import QualificationQuestionAdd, questionary_success_created


urlpatterns = [
    path('questionary-creating/', QualificationQuestionAdd.as_view(), name="questionary-creating"),
    path("questionary-success/", questionary_success_created, name='questionary-success'),

    path("qualification-question/<int:pk>", QualificationQuestionGet.as_view()),
    path("qualification-question-list/", QualificationQuestionList.as_view()),
    path("qualification-question-create/", QualificationQuestionCreate.as_view()),

    path("feature-question/<int:pk>", FeatureQuestionGet.as_view()),
    path("feature-question-list/", FeatureQuestionList.as_view()),
    path("feature-question-create/", FeatureQuestionCreate.as_view()),

    path("questionary-create/", QuestionaryCreate.as_view()),
]