import boto3
import json
from collections import Counter

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('PostsTable')

    # Scan the table to get all items
    response = table.scan()
    items = response['Items']
    
    # Collect all hashtags
    hashtags = []
    for item in items:
        hashtags.extend(item.get('hashtags', []))
    
    # Count occurrences of each hashtag
    hashtag_counts = Counter(hashtags)
    
    # Convert counts to a list of tuples
    trending_hashtags = [{'hashtag': hashtag, 'count': count} for hashtag, count in hashtag_counts.items()]
    
    return {
        'statusCode': 200,
        'body': json.dumps(trending_hashtags)
    }