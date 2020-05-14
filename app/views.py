from django.http import HttpResponse
from dwebsocket.decorators import accept_websocket,require_websocket
import json

@accept_websocket
def websocket_noly_api(request):
    if request.is_websocket():

        for message in request.websocket:  # 客户端刷新/关闭时, message 为 None
            if message:

                request.websocket.send(json.dumps({"a":"a"}))
            else:
                break

    return HttpResponse("Api")