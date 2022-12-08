from django import forms
from django.contrib.auth import authenticate

from . import models


class UserLoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = models.UserModel
        fields = ('username', 'password')

    def authenticate(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        return authenticate(username=username, password=password)


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.UserModel
        fields = (
            'login', 'email', "phone", "password1", "password2",
            'firstname', 'lastname', 'role'
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user
