from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

import hmac
import hashlib
import json
import logging
LOG = logging.getLogger(__name__)

# Create your views here.
@csrf_exempt
def index(request):
    _body = request.body.decode("utf-8")
    print("type: %s" % type(request.body))
    try:
        _body = json.loads(_body)
    except:
        pass
    header_signature = request.headers.get('X-Hub-Signature')
    print("============================================")
    print("Header Signature: %s" % header_signature)
    print("============================================")
    mac = hmac.new(bytes("secret", "utf-8"), msg=request.body, digestmod=hashlib.sha1)
    print("============================================")
    print(mac.hexdigest())
    print("============================================")
    print("api_post.header: %s" % json.dumps(
        request.headers.__dict__, indent=4
    ))
    return JsonResponse({
        "header": request.headers.__dict__,
        "mac": mac.hexdigest()
    })
