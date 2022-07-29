import base64
import json
from pathlib import Path
from server.common.util import get_spec_path


def handler(event, context):
    result = ("Error", 501)
    if 'requestContext' in event and 'operationName' in event['requestContext']:
        req = event['requestContext']
        method_name = req['operationName']
        method = globals()[method_name]
        print(req)
        if 'body' in event and event['body']:
            result = method(json.loads(event['body']))
        else:
            result = method()
    return response_proxy(content=result[0],
                          status_code=result[1],
                          headers=result[2] if len(result) >= 3 else None,
                          isBase64Encoded=result[3] if len(result) >= 4 else False)


def response_proxy(content, status_code, headers=None, isBase64Encoded=False):
    response = {
        'isBase64Encoded': isBase64Encoded,
        'statusCode': status_code,
        'body': json.dumps(content) if not isBase64Encoded else base64.encodebytes(content),
        'headers': {}
    }
    if headers:
        response["headers"] = headers
    return response


def getSpec():
    return Path(get_spec_path()).read_bytes(), 200, None, True


def getServiceDescription():
    return "No Content", 204, {"Link": '</spec>; rel="service-desc"'}


def getHealth():
    return "Healthy as a rock", 200


def postCalculate(payload):
    result = {
        'result': payload['a'] + payload['b']
    }
    return result, 200
