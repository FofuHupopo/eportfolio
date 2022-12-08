from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest


class AccountView(View):
    def get(self, request: HttpRequest):
        return render(
            request,
            "account__account.html",
            {}
        )


class UpdateInformationView(View):
    def post(self, request: HttpRequest):
        ...
