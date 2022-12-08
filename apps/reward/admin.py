from django.contrib import admin

from . import models


admin.site.register(models.RewardModel)
admin.site.register(models.RewardCategoryModel)
admin.site.register(models.RewardTypeModel)
