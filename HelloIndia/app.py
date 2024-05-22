import json 
def lambda_handler(event, context):
    print("Hello India")
    return {
        "statusCode": 200,
        "body": json.dumps("Hello India")
    }