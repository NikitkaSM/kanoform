from django.contrib import admin
from .models import Questionary, QualificationQuestion, FeatureQuestion, FeatureResponse, QualificationResponse, Response, Feedback


admin.site.register(Questionary)
admin.site.register(QualificationQuestion)
admin.site.register(FeatureQuestion)
admin.site.register(FeatureResponse)
admin.site.register(QualificationResponse)
admin.site.register(Response)
admin.site.register(Feedback)
