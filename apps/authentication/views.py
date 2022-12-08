from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.views import View
from django.http.request import HttpRequest
# from django.contrib.auth.decorators import not

from . import forms


class LoginView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect("account")

        return render(
            request,
            "auth__login.html"
        )

    def post(self, request: HttpRequest):
        form = forms.UserLoginForm(request.POST)

        if form.is_valid():
            user = form.authenticate()

            if user:
                login(request, user)
                return redirect("account")

        return render(
            request,
            "auth__login.html"
        )


class RegistrationView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect("account")

        step = self.get_step(request)

        if step == "1":
            return self.get__first_step(request)

        return self.get__second_step(request)

    @staticmethod
    def get__first_step(request: HttpRequest):
        return render(
            request,
            "auth__registration1.html"
        )

    def get__second_step(self, request: HttpRequest):
        if "form" not in request.session:
            self.min_step(request)
            return self.get(request)

        return render(
            request,
            "auth__registration2.html"
        )

    def post(self, request: HttpRequest):
        step = self.get_step(request)

        if step == "1":
            return self.post__first_step(request)

        return self.post__second_step(request)

    def post__first_step(self, request: HttpRequest):
        request.session["form"] = request.POST

        self.add_step(request)
        return self.get(request)

    def post__second_step(self, request: HttpRequest):
        self.min_step(request)

        if "form" not in request.session:
            return self.get(request)

        first_page_data = request.session.get("form")
        form = forms.UserRegistrationForm(
            {
                **first_page_data,
                **request.POST.dict()
            }
        )

        if form.is_valid():
            form.save()
            return redirect("login")

        return render(
            request,
            "auth__registration1.html",
            {
                "errors": form.errors
            }
        )

    @staticmethod
    def get_step(request: HttpRequest):
        if "step" not in request.session or request.session.get("step") not in ("1", "2"):
            request.session["step"] = "1"

        return request.session.get("step")

    @staticmethod
    def add_step(request: HttpRequest):
        request.session["step"] = "2"

    @staticmethod
    def min_step(request: HttpRequest):
        request.session["step"] = "1"


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("login")
