from django.urls import path
from .views import FeatureQuestionCreate, FeatureQuestionList, QualificationQuestionAdd, questionary_success_created, \
    QualificationQuestionCreate, QualificationQuestionList

urlpatterns = [
    path('questionary-creating/', QualificationQuestionAdd.as_view(), name="questionary-creating"),
    path("questionary-success/", questionary_success_created, name='questionary-success'),
    path("qualification-question/", QualificationQuestionList.as_view()),
    path("qualification-question-create/", QualificationQuestionCreate.as_view()),
    path("feature-question/", FeatureQuestionList.as_view()),
    path("feature-question-create/", FeatureQuestionCreate.as_view()),
]