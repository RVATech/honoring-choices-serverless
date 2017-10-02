"""
Provides a simple RDS query

Envionrment Variables:
    DB_USER
    DB_DATABASE
    DB_HOST
    DB_PASSWORD
"""
from json import dumps
from os import getenv
import pymysql


def lambda_handler(event, context):
    connection = get_database_connection()
    cursor = connection.cursor()
    pages = get_page_data(cursor)
    cursor.close()
    connection.close()
    return returnGatewayResponse(pages)


def returnGatewayResponse(body):
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {'content-type': 'application/json'},
        'body': str(dumps(body))
    }


def get_database_connection():
    return pymysql.connect(
        host=getenv('DB_HOST'),
        user=getenv('DB_USER'),
        db=getenv('DB_DATABASE'),
        password=getenv('DB_PASSWORD'),
        cursorclass=pymysql.cursors.DictCursor
    )


def get_page_data(cursor):
    query = ("SELECT body FROM pages")
    cursor.execute(query)

    return cursor.fetchall()
