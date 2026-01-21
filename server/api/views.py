from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import DataPoint

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
    return JsonResponse(data, safe=False)

