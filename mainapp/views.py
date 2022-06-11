from django.http import HttpResponse
import json
import requests
from django.shortcuts import render


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


def index(request):
    return render(request, 'login.html')
    # HttpResponse(jprint(response.json()['puuid']))


def dashboard(request):
    ign = request.POST['username']
    tag = request.POST['password']
    apiserver = 'https://api.henrikdev.xyz'
    req = apiserver + '/valorant/v1/mmr-history/ap/' + ign + '/' + tag
    response1 = requests.get(req)
    array=response1.json()['data']
    rank=array[0]['currenttierpatched']
    str1=''
    for i in array:
        elo=i['elo']
        str1=str1+str(elo)+'\r\n'
    return HttpResponse("Hey, "+ign+"\r\n Your current rank is "+rank+"\r\nLast 10 matches ELO (Latest First):\r\n "+str1,content_type="text/plain")