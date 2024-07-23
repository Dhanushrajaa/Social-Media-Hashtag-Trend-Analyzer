import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PostsTable')

def lambda_handler(event, context):
    post_content = event['post_content']
    hashtags = [word for word in post_content.split() if word.startswith('#')]
    
    try:
        response = table.put_item(
            Item={
                'post_id': str(context.aws_request_id),
                'post_content': post_content,
                'hashtags': hashtags
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Post processed and stored successfully!')
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed to store post: {e.response['Error']['Message']}")
        }