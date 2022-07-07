from django.urls import path
from questionary.views import qualification_question_add, questionary_success_created, questionary_list


urlpatterns = [
    path('questionary-creating/', qualification_question_add, name="questionary-creating"),
    path("questionary-success/", questionary_success_created, name='questionary-success'),
    path("questionary-list/", questionary_list)
]
