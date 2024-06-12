from django.contrib import admin
from django.urls import include, path

from pybo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("common/", include("common.urls")),
    path("pybo/", include("pybo.urls")),

    # DRF
    path('api-auth/', include('rest_framework.urls')),
    path('api/pybo/', include('pybo.api_urls')),
]
