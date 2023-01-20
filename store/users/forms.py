from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserChangeForm,
    UserCreationForm
)
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
                'type': 'username',
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'type': 'first_name',
            }
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'type': 'last_name',
            }
        )
    )
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
                'type': 'username',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
                'type': 'email',
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
                'type': 'password',
            }
        )
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Подтверждение пароля',
                'type': 'password',
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'first_name',
            }
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'last_name',
            }
        )
    )
    username = forms.CharField(
        required=False,
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'username',
                'readonly': True,
            }
        )
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'readonly': True,
            }
        )
    )
    image = forms.ImageField(
        required=False,
        label='Аватар',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'type': 'file',
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'image',
        )
