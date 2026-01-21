from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def data_mock(request):
    data = {
        "sensor": "temperature",
        "value": 23.5,
        "unit": "Celsius",
        "ts": "2024-06-01T12:00:00Z"
    }
    return JsonResponse(data)

