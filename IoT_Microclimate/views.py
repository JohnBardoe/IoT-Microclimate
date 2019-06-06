import datetime
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from IoT_Microclimate.models import DataFrame


@csrf_exempt
def setDataFrame(request):
    if request.method != 'GET':
        return
    data = request.GET
    df = DataFrame()
    df.id = int(data["id"])
    df.temp = float(data["temp"])
    df.humidity = int(data["humidity"])
    df.pressure = int(data["pressure"])
    df.co2 = int(data["co2"])
    df.co = int(data["co"])
    df.charge = int(data["charge"])
    df.time = datetime.time()
    df.save()
    print('DataFrame request: ', df)
    return HttpResponse('OK')

def makeCharts():


def index(request):
    return render(request, "index.html", {})

