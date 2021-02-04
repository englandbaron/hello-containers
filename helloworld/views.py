from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

import json
import logging
LOG = logging.getLogger(__name__)

# Create your views here.
@csrf_exempt
def index(request):
    _body = request.body.decode("utf-8")
    try:
        _body = json.loads(_body)
    except:
        pass
    LOG.info("api_post.body: %s" % json.dumps(_body, indent=4))
    LOG.info("api_post.header: %s" % json.dumps(
        request.headers.__dict__, indent=4
    ))
    return JsonResponse({
        "data": _body,
        "header": request.headers.__dict__
    })
