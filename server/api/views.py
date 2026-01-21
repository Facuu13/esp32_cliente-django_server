from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import DataPoint
from django.utils import timezone

def data_list(request):
    data_points = DataPoint.objects.all().order_by('-ts')[:10]
    data = []
    for dp in data_points:
        data.append({
            "source": dp.source,
            "key": dp.key,
            "value": float(dp.value),
            "ts": dp.ts.isoformat(),
        })
    payload = {
        "schema_version": "1",
        "generated_at": timezone.now().isoformat(),
        "count": len(data),
        "data": data,
    }
    return JsonResponse(payload)

