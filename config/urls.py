import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("core/", include("src.core.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("src.users.urls")),
    path("houses/", include("src.houses.urls")),
    path("apartments/", include("src.apartments.urls")),
    path("statistic/", include("src.statistic.urls")),
    path("system/settings/", include("src.service.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
