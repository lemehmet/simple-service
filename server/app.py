import json

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
    return response_proxy(result[0], result[1], result[2] if len(result) >= 3 else None)


def response_proxy(content, status_code, headers=None):
    response = {
        'isBase64Encoded': False,
        'statusCode': status_code,
        'body': json.dumps(content),
        'headers': {}
    }
    if headers:
        response["headers"] = headers
    return response


def getSpec():
    spec_path = get_spec_path()
    content = "Nothing"
    with open(spec_path, 'r') as f:
        content = f.read()
    return content, 200


def getServiceDescription():
    return "No Content", 204, {"Link": '</spec>; rel="service-desc"'}


def getHealth():
    return "Healthy as a rock", 200


def postCalculate(payload):
    result = {
        'result': payload['a'] + payload['b']
    }
    return result, 200
