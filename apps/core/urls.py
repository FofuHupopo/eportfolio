from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path('information/', login_required(views.InformationView.as_view()), name="information"),
    path('classes/', login_required(views.ClassesView.as_view()), name="classes"),
    path('classes/<int:pk>/', login_required(views.DetailClassView.as_view()), name="detail_class"),
    path('add_student_to_class/<int:class_pk>/', login_required(views.AddStudentToClass.as_view()), name="add_student_to_class")
]
