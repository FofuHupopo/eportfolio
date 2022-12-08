from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path("", login_required(views.AccountView.as_view()), name="account"),
    path("update-main-information/", login_required(views.UpdateInformationView.as_view()), name="update_information")
]
