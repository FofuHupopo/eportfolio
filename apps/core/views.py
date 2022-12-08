from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views import View
from django.http.request import HttpRequest

from . import models


class InformationView(View):
    def get(self, request: HttpRequest):
        return render(
            request,
            "core__information.html"
        )


class ClassesView(View):
    def get(self, request: HttpRequest):
        if request.user.is_staff:
            classes = models.ClassModel.objects.all()
        else:
            classes = models.ClassModel.get_user_class(request.user)

        return render(
            request,
            "core__classes.html",
            {
                "classes": classes
            }
        )


class DetailClassView(View):
    def get(self, request: HttpRequest, pk: int):
        class_ = get_object_or_404(
            models.ClassModel,
            pk=pk
        )

        return render(
            request,
            "core__class.html",
            {
                "class": class_
            }
        )


class AddStudentToClass(View):
    def post(self, request: HttpRequest, class_pk: int):
        student_id = request.POST.get("student_id")
        
        class_: models.ClassModel = models.ClassModel.objects.get(
            pk=class_pk
        )
        
        class_.students.add(
            get_user_model().objects.get(
                pk=student_id
            )
        )
        
        return redirect("detail_class", class_pk)
