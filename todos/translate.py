import os
import json
import logging
from todos import decimalencoder
import boto3

translate = boto3.client('translate')

dynamodb = boto3.resource('dynamodb')
firehose = boto3.client('firehose')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
logger = logging.getLogger()
logger.setLevel(logging.INFO)

SRC_LANG = 'en'

def lambda_handler(event, context):
    logger.info(event)
    data = json.loads(event['body'])
    if 'id' in event and 'target_language' in event and 'text' in event :
        review_id = event['id']
        target_language = event['target_language']
        text = event['text']

   
