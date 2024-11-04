from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("core/", include("src.core.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("src.users.urls")),  # path to statistic
    path("statistic/", include("src.statistic.urls")),  # path to statistic
]
