from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path("my-rewards/", login_required(views.RewardView.as_view()), name="rewards"),
    path("rewards/<int:class_pk>/<int:user_pk>/", login_required(views.StudentRewardView.as_view()), name="student_rewards"),
    path('add-reward/<int:user_pk>/', login_required(views.AddRewardView.as_view()), name="add-reward-pk"),
    path('add-reward/', login_required(views.AddRewardView.as_view()), name="add-reward"),
]
