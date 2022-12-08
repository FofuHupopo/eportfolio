from django import forms

from . import models


class RewardForm(forms.ModelForm):
    class Meta:
        model = models.RewardModel
        fields = "__all__"
        exclude = ('user',) 
