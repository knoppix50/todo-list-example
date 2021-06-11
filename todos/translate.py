import os
import json
import logging
from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

def translate(event, context):
    translater = boto3.client('translate')
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    target_language = event['pathParameters']['id']['target_language']
    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder, target_language)
    }

    return response
    

   