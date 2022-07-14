from django.urls import path
from questionary.views import questionary_creating, questionary_success_created, questionary_list, questionary_fill_in

urlpatterns = [
    path('questionary-creating/', questionary_creating, name="questionary-creating"),
    path("questionary-success/", questionary_success_created, name='questionary-success'),
    path("questionary-list/", questionary_list),
    path("<int:pk>", questionary_fill_in)
]
