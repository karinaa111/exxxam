from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from branches_app import views

schema_view = get_schema_view(
    openapi.Info(
        title="Branches API",
        default_version="v1",
        description="API для управління філіями",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", views.home, name="home"),
    path("branches/", views.branches_list, name="branches-list"),
    path("branches/<int:pk>/", views.branch_update, name="branches-update"),

    # Swagger UI
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r"^swagger\.json$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]
