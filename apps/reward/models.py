from django.db import models
from django.db.models.manager import Manager
from django.contrib.auth import get_user_model


class RewardCategoryModel(models.Model):
    name = models.CharField(
        verbose_name="Название категории", max_length=128
    )

    objects = Manager()

    class Meta:
        db_table = 'reward__category'
        verbose_name = 'Категория награды'
        verbose_name_plural = 'Категории наград'

    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"


class RewardTypeModel(models.Model):
    name = models.CharField(
        verbose_name="Название типа", max_length=128
    )

    objects = Manager()

    class Meta:
        db_table = 'reward__type'
        verbose_name = 'Тип награды'
        verbose_name_plural = 'Типы наград'

    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"


class RewardModel(models.Model):
    name = models.CharField(
        verbose_name="Название награды", max_length=128
    )
    description = models.TextField(
        verbose_name="Описание награды",
        null=True, blank=True
    )
    type = models.ForeignKey(
        RewardTypeModel, models.CASCADE,
        verbose_name="Тип награды"
    )
    categories = models.ManyToManyField(
        RewardCategoryModel, blank=True,
        verbose_name="Категории награды"
    )
    photo = models.ImageField(
        "Фото награды", upload_to="reward_photo/",
        null=True, blank=True
    )
    user = models.ForeignKey(
        get_user_model(), models.CASCADE,
        null=True, blank=True,
        verbose_name="Пользователь"
    )

    objects = Manager()

    class Meta:
        db_table = "reward__reward"
        verbose_name = 'Награда'
        verbose_name_plural = "Награды"

    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"

    @staticmethod
    def get_user_rewards(user):
        return RewardModel.objects.filter(user=user)
