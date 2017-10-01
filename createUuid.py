from uuid import uuid4
from json import dumps


def lambda_handler(event, context):
    body = {'uuid': str(uuid4())}
    return returnGatewayResponse(body)


def returnGatewayResponse(body):
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {'content-type': 'application/json'},
        'body': str(dumps(body))
    }
