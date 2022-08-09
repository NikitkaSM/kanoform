from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1',)


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')