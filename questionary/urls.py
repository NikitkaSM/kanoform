from django.urls import path
from questionary.views import QualificationQuestionAdd, questionary_success_created, QuestionaryList


urlpatterns = [
    path('questionary-creating/', QualificationQuestionAdd.as_view(), name="questionary-creating"),
    path("questionary-success/", questionary_success_created, name='questionary-success'),
    path("questionary-list/", QuestionaryList.as_view())
]
