import django
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Questionary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50, default="My Form")
    created_time = models.DateTimeField(default=django.utils.timezone.now, blank=True)

    class Meta:
        verbose_name_plural = "Questionary"

    def __str__(self):
        return self.name


class QualificationQuestion(models.Model):
    questionary = models.ForeignKey(
        Questionary,
        on_delete=models.CASCADE,
        related_name="qualification_questions",
        blank=True)
    question = models.TextField(max_length=150)
    answer_variants = ArrayField(
        models.TextField(max_length=100, blank=True),
    )
    is_multiple = models.BooleanField(null=True)

    class Meta:
        verbose_name_plural = "QualificationQuestion"

    def __str__(self):
        return self.question


class FeatureQuestion(models.Model):
    questionary = models.ForeignKey(
        Questionary,
        on_delete=models.CASCADE,
        related_name='feature_questions',
        blank=True)
    feature_name = models.CharField(max_length=50)
    feature_description = models.TextField(max_length=250)

    class Meta:
        verbose_name_plural = "FeatureQuestion"

    def __str__(self):
        return self.feature_name


class FeatureResponse(models.Model):
    feature_question = models.ForeignKey(FeatureQuestion,
                                         on_delete=models.CASCADE)
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.IntegerField()
    response = models.ForeignKey(
        "Response",
        on_delete=models.CASCADE,
        related_name="feature_response")

    class Meta:
        verbose_name_plural = "FeatureResponse"


class QualificationResponse(models.Model):
    qualification_question = models.ForeignKey(
        QualificationQuestion,
        on_delete=models.CASCADE)
    response = models.ForeignKey(
        "Response",
        on_delete=models.CASCADE,
        related_name="qualification_response", null=True)
    answer = models.TextField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "QualificationResponse"


class Response(models.Model):
    questionary = models.ForeignKey(Questionary, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Response"


class Feedback(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE, null=True, related_name="feedback", blank=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    messenger = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Feedback"
