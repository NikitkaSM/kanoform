from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.views import APIView
from .forms import FeedbackForm, QuestionaryForm, FeatureQuestionForm, QualificationAnswerVariantForm, qualificationQuestionFormset
from .models import Feedback, Questionary, QualificationQuestion, FeatureQuestion
from django.contrib.auth.models import User
from .services import QualificationQuestionsBaseModel, FeatureQuestionsBaseModel
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from .serializers import FeatureQuestionSerializer, QualificationQuestionSerializer, \
    QualificationQuestionCreateSerializer


def questionary_success_created(request):
    return render(request, "questionary/questionary_success_create.html")


@method_decorator(staff_member_required, name="dispatch")
class QualificationQuestionAdd(TemplateView):
    template_name = "questionary/form_create.html"

    def get(self, *args, **kwargs):
        formset = qualificationQuestionFormset(queryset=QualificationQuestion.objects.none())

        context = {
            "qualification_question_formset": formset,
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        feedback_form = FeedbackForm(request.POST)
        questionary_form = QuestionaryForm(request.POST)
        qualification_answer_variant_form = QualificationAnswerVariantForm(request.POST)
        feature_question_form = FeatureQuestionForm(request.POST)
        qualification_question_formset = qualificationQuestionFormset(queryset=QualificationQuestion.objects.none())

        if questionary_form.is_valid():
            Questionary.objects.create(name=request.POST.get("questionary_name"),
                                       user=User.objects.get(username=request.user.get_username()))

        questionary_name = Questionary.objects.get(name=request.POST.get("questionary_name"))

        if qualification_question_formset.is_valid():
            qualification_question = request.POST.get("qualification_question")
            # qualification_question_dict = {"question": qualification_question}
            # qualification_question = request.POST.get("qualification_question")

            if qualification_answer_variant_form.is_valid():
                answer_variant = request.POST.get("answer_variant")
                QualificationQuestion.objects.create(
                    questionary=questionary_name,
                    question="{" + qualification_question + '}',
                    answer_variants="{" + answer_variant + '}')

        if feature_question_form.is_valid():
            feature_question = request.POST.get("feature_question")
            FeatureQuestion.objects.create(
                questionary=questionary_name,
                feature_name=request.POST.get("feature_question"),
                feature_description=request.POST.get("feature_description"))

        if feedback_form.is_valid():
            email = request.POST.get("email")
            phone_number = request.POST.get("phone_number")
            messenger = request.POST.get("messenger")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")

            Feedback.objects.create(
                email=email,
                phone_number=phone_number,
                messenger=messenger,
                first_name=first_name,
                last_name=last_name,
            )
            return HttpResponseRedirect("/questionary-success")

        context = {
            "feedback": feedback_form,
            "questionary": questionary_form,
            "qualification_answers": qualification_answer_variant_form,
            "feature_question": feature_question_form,
            "qualification_question_formset": qualification_question_formset,
        }

        return self.render_to_response(context)


class QualificationQuestionList(APIView):
    def get(self, request):
        qualification_question = QualificationQuestion.objects.all()
        serializer = QualificationQuestionSerializer(qualification_question, many=True)

        serializer_in_json = QualificationQuestionsBaseModel(questions=serializer.data)

        parsed_json = serializer_in_json.dict()

        return Response(parsed_json)


class QualificationQuestionCreate(APIView):
    def post(self, request):
        serializer = QualificationQuestionCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response("success created")


class FeatureQuestionList(APIView):
    def get(self, request):
        question = FeatureQuestion.objects.all()
        serializer = FeatureQuestionSerializer(question, many=True)

        serializer_in_json = FeatureQuestionsBaseModel(questions=serializer.data)

        parsed_data = serializer_in_json.dict()

        return Response(parsed_data)


class FeatureQuestionCreate(APIView):
    def post(self, request):
        serializer = FeatureQuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response("success created")
