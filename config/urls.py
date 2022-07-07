from django.contrib import admin
from django.urls import path, include
from users.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('landing/', landing, name='landing'),
    path('questionaries/', include('questionary.urls')),
    path("api/", include("api.urls"))
]
