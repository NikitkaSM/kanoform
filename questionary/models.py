from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Questionary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="My Form")

    class Meta:
        verbose_name_plural = "Questionary"

    def __str__(self):
        return self.name


class QualificationQuestion(models.Model):
    questionary = models.ForeignKey(Questionary, on_delete=models.CASCADE)
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
        related_name='feature_questions')
    feature_name = models.CharField(max_length=50)
    feature_description = models.TextField(max_length=250)

    class Meta:
        verbose_name_plural = "FeatureQuestion"


class FeatureResponse(models.Model):
    feature_question = models.ForeignKey(FeatureQuestion,
                                         on_delete=models.CASCADE)
    answer_1 = models.IntegerField()
    answer_2 = models.IntegerField()
    answer_3 = models.IntegerField()
    features_answers = models.ForeignKey(
        "Response",
        on_delete=models.CASCADE,
        related_name="features_answers")

    class Meta:
        verbose_name_plural = "FeatureResponse"


class QualificationResponse(models.Model):
    qualification_question = models.ForeignKey(
        QualificationQuestion,
        on_delete=models.CASCADE)
    qualification_answers = models.ForeignKey(
        "Response",
        on_delete=models.CASCADE,
        related_name="qualification_answers")

    class Meta:
        verbose_name_plural = "QualificationResponse"


class Response(models.Model):
    questionary = models.ForeignKey(Questionary, on_delete=models.CASCADE)
    feedback = models.ForeignKey(
        "Feedback", on_delete=models.DO_NOTHING,
        null=True)

    class Meta:
        verbose_name_plural = "Response"


class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    messenger = models.TextField()
    phone_number = models.TextField()
    email = models.CharField(max_length=75)

    class Meta:
        verbose_name_plural = "Feedback"
