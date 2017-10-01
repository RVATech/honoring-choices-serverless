from uuid import uuid4


def lambda_handler(event, context):
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {'content-type': 'application/json'},
        'body': str({'uuid': str(uuid4())})
    }
