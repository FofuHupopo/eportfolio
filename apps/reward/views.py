from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from typing import List
from django.http.request import HttpRequest
from django.core.handlers.wsgi import WSGIRequest

from . import forms
from . import models
from apps.core.models import ClassModel


class RewardView(View):
    def get(self, request: WSGIRequest):
        rewards: List[models.RewardModel] = models.RewardModel.get_user_rewards(request.user)

        return render(
            request,
            "reward__rewards.html",
            {
                "rewards": rewards
            }
        )


class StudentRewardView(View):
    def get(self, request: WSGIRequest, class_pk: int, user_pk: int):
        student = get_object_or_404(
            get_user_model(),
            pk=user_pk
        )
        rewards: List[models.RewardModel] = models.RewardModel.get_user_rewards(student)

        return render(
            request,
            "reward__students_rewards.html",
            {
                "rewards": rewards,
                "student": student,
                "class_pk": class_pk,
            }
        )


class AddRewardView(View):
    def get(self, request: WSGIRequest, user_pk=None):
        form = forms.RewardForm()
        
        return render(
            request,
            'reward__add_reward.html',
            {
                "form": form
            }
        )
        
    def post(self, request: WSGIRequest, user_pk=None):
        user = user_pk or request.user

        form = forms.RewardForm(
            request.POST, request.FILES
        )

        if form.is_valid():            
            reward = form.save(commit=False)
            reward.user = get_user_model().objects.get(pk=user)
            reward.save()
            
            if user_pk:
                class_: ClassModel = ClassModel.objects.filter(students=user_pk).first()
            
                return redirect("student_rewards", class_.pk, user_pk)
            
            return redirect("rewards")
        
        print(form.errors)
        
        return self.get(request)
