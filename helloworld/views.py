from django.shortcuts import HttpResponse
from django.shortcuts import render

import json

# Create your views here.
def index(request):
    return HttpResponse(json.dumps({"Echo":"HELLO WORLD"}))