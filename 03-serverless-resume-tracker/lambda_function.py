import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("resume-tracker")


def lambda_handler(event, context):
    body = json.loads(event["body"])

    table.put_item(
        Item={
            "applicationID": body["applicationID"],
            "company": body["company"],
            "position": body["position"],
            "status": body["status"]
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Application saved successfully!")
    }