from django.urls import path, include


urlpatterns = [
    path("auth/", include("apps.authentication.urls")),
    path("reward/", include("apps.reward.urls")),
    path("account/", include("apps.account.urls")),
    path("", include('apps.core.urls')),
]
