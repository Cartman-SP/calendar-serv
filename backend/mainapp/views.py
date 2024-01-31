from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@csrf_exempt
def receive_data(request):
    print(request)
    try:
        data = json.loads(request.body)
        return JsonResponse({"status": "success", "data": data})
    except json.JSONDecodeError as e:
        return JsonResponse({"status": "error", "message": f"Invalid JSON: {str(e)}"}, status=400)