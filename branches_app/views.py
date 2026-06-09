import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Branch


def home(request):
    """Головна сторінка зі списком філій."""
    return render(request, "branches_app/index.html", {
        "branches": Branch.objects.all().order_by("id"),
    })


branch_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID філії"),
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="Назва філії"),
        "address": openapi.Schema(type=openapi.TYPE_STRING, description="Адреса"),
        "phone": openapi.Schema(type=openapi.TYPE_STRING, description="Телефон"),
    },
)

branch_update_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="Назва філії"),
        "address": openapi.Schema(type=openapi.TYPE_STRING, description="Адреса"),
        "phone": openapi.Schema(type=openapi.TYPE_STRING, description="Телефон"),
    },
)


@swagger_auto_schema(
    method="get",
    operation_summary="Список філій",
    operation_description="Повертає список усіх філій у форматі JSON.",
    responses={200: openapi.Response("Список філій", openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={"branches": openapi.Schema(type=openapi.TYPE_ARRAY, items=branch_schema)},
    ))},
)
@api_view(["GET"])
def branches_list(request):
    """GET /branches/ — Повертає список усіх філій."""
    branches = Branch.objects.all().order_by("id")
    return Response({"branches": [b.to_dict() for b in branches]})


@swagger_auto_schema(
    method="put",
    operation_summary="Оновити філію",
    operation_description="Оновлює поля name, address, phone для вказаної філії.",
    request_body=branch_update_schema,
    responses={
        200: openapi.Response("Оновлена філія", openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"branch": branch_schema},
        )),
        404: "Філію не знайдено",
        400: "Невалідний JSON",
    },
)
@api_view(["PUT"])
def branch_update(request, pk):
    """PUT /branches/<id>/ — Оновити дані філії."""
    try:
        payload = request.data
    except Exception:
        return Response({"error": "Невалідний JSON"}, status=400)

    try:
        branch = Branch.objects.get(pk=pk)
    except Branch.DoesNotExist:
        return Response({"error": f"Філію id={pk} не знайдено"}, status=404)

    for field in ("name", "address", "phone"):
        if field in payload:
            setattr(branch, field, payload[field])
    branch.save()
    return Response({"branch": branch.to_dict()})
