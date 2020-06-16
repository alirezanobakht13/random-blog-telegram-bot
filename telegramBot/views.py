from django.shortcuts import render
from django.http import JsonResponse
import json
from .telegram.Telegram import TelegramBot
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def bot_response(request):
    body = json.loads(request.body)
    tele = TelegramBot(body)
    res = tele.action()
    return JsonResponse({'success':res,})