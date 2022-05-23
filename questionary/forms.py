from django import forms
from django.forms import modelformset_factory
from .models import QualificationQuestion


class QuestionaryForm(forms.Form):
    questionary_name = forms.CharField()


qualificationQuestionFormset = modelformset_factory(
    QualificationQuestion, fields=("question",), extra=1
)

qualificationAnswerFormset = modelformset_factory(
    QualificationQuestion, fields=("answer_variants",), extra=0
)


class QualificationAnswerVariantForm(forms.Form):
    answer_variant = forms.CharField()


class FeatureQuestionForm(forms.Form):
    feature_question = forms.CharField()
    feature_description = forms.CharField()


class FeedbackForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    messenger = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField()
