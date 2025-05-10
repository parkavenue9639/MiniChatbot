# chat/views.py
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

LLAMA_SERVER_URL = 'http://localhost:8001/predict/'

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt", "")
            if not prompt:
                return JsonResponse({"error": "Missing prompt."}, status=400)

            llama_payload = {
                "prompt": prompt,
                "n_predict": 128
            }

            response = requests.post(LLAMA_SERVER_URL, json=llama_payload, timeout=30)
            response.raise_for_status()

            result = response.json()
            return JsonResponse({"response": result.get("response", "")})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST allowed."}, status=405)