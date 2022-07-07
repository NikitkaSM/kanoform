from django.contrib.admin.views.decorators import staff_member_required
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpResponseNotFound


def questionary_success_created(request):
    if not request.user:
        return HttpResponseNotFound("access denied")

    csrf_token = get_token(request)
    csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)
    return render(request, "questionary/questionary_success_create.html")


class QuestionaryList(TemplateView):
    template_name = 'questionary/questionary-list.html'


@method_decorator(staff_member_required, name="dispatch")
class QualificationQuestionAdd(TemplateView):
    template_name = "questionary/questionary-creating.html"
