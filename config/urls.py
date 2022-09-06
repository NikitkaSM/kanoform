from django.contrib import admin
from django.urls import path, include, re_path
from users.views import landing
from django.views.generic.base import RedirectView


handler404 = "questionary.views.handler404"
handler500 = "questionary.views.handler500"
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('landing/', landing, name='landing'),
    path('questionaries/', include('questionary.urls')),
    path("api/", include("api.urls")),
]
