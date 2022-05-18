from django.urls import path
from .views import register, profile, login, logout


urlpatterns = [
    path('register/', register, name="register"),
    path('profile/', profile, name="user_profile"),
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
]
