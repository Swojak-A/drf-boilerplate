from django.urls import include, path

from config import settings

app_name = "api"

urlpatterns = [
    path(
        "healthchecks/", include("modules.healthchecks.urls", namespace="healthchecks")
    ),
]
