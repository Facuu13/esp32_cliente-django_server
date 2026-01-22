from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import DataPoint
from django.utils import timezone



def data_list(request):
    DEFAULT_LIMIT = 10
    MAX_LIMIT = 50
    limit_str = request.GET.get("limit")
    if limit_str is None:
        limit = DEFAULT_LIMIT
    else:
        try:
            limit = int(limit_str)
        except ValueError:
            return JsonResponse({"status": "error", 
                                 "error": {
                                     "code": "invalid_parameter", 
                                     "message": "Invalid limit parameter"
                                     }
                                }, status=400)
        if limit <= 0:
            return JsonResponse({
                "status": "error",
                "error": {
                    "code": "invalid_limit",
                    "message": "limit must be a positive integer"
                        }
                }, status=400)
        if limit > MAX_LIMIT:
            limit = MAX_LIMIT
    data_points = DataPoint.objects.all().order_by('-ts')[:limit]

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

