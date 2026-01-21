from django.http import HttpResponse, JsonResponse

def hola_mundo(request):
    return HttpResponse("Hola mundo!")

def hola_mundo_json(request):
    response = {
        "status": "ok",
        "data": {
            "message": "Hola desde la API",
            "number": 42
        }
    }
    return JsonResponse(response)