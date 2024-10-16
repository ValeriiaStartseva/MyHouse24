from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("core/", include("src.core.urls")),
    path("admin/", admin.site.urls),
]
