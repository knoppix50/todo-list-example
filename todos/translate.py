import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

def getTranslated(event, context):
    translate = boto3.client('translate')
    source_language = 'en'
    target_language = event['pathParameters']['target_language']
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    recordset = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    texto = (recordset['Item']['text'])
    
    #result = translater.translate_text(Text='Hello, my name is Alfredo.', SourceLanguageCode=source_language, TargetLanguageCode=target_language)
    result = translate.translate_text(Text=texto, SourceLanguageCode=source_language, TargetLanguageCode=target_language)
    
    response = {
        'statusCode': 200,
        'body': json.dumps(result['TranslatedText'])
        
    }
    
    return response
