from django.db import models
from django.db.models.manager import Manager
from django.contrib.auth import get_user_model


class ClassModel(models.Model):
    name = models.CharField(
        "Название класса", max_length=128
    )
    teacher = models.ForeignKey(
        get_user_model(), models.CASCADE,
        verbose_name="Учитель", related_name="teacher"
    )
    students = models.ManyToManyField(
        get_user_model(), blank=True,
        verbose_name="Ученики", related_name="students"
    )

    objects = Manager()

    class Meta:
        db_table = "core__class"
        verbose_name = 'Класс'
        verbose_name_plural = "Классы"

    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"

    @staticmethod
    def get_user_class(user):
        return ClassModel.objects.filter(teacher=user)
