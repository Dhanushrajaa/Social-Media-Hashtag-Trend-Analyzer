import streamlit as st
import boto3
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv("AWS_Credential.env")

# Get AWS credentials from environment variables
region_name = os.getenv('AWS_REGION_NAME')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Set the title of the app
st.title("Social Media Hashtag Trend Analyzer")

# Create a text area for composing the post
post_content = st.text_area("Compose your post here...", height=200)

# Initialize AWS Lambda client
lambda_client = boto3.client(
    'lambda',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Button to submit the post
if st.button("Post"):
    if post_content:
        payload = {'post_content': post_content}
        try:
            response = lambda_client.invoke(
                FunctionName='ProcessPostFunction',
                InvocationType='RequestResponse',
                Payload=json.dumps(payload)
            )
            response_payload = json.loads(response['Payload'].read())
            if response_payload['statusCode'] == 200:
                st.success("Your post has been published and processed!")
            else:
                st.error(f"Error: {response_payload['body']}")
        except Exception as e:
            st.error(f"Error invoking Lambda function: {str(e)}")
    else:
        st.error("Please write something before posting.")

# Button to show trending hashtags
if st.button("Show Trending Hashtags"):
    try:
        response = lambda_client.invoke(
            FunctionName='TrendingHashtagsFunction',
            InvocationType='RequestResponse',
            Payload=json.dumps({})
        )
        response_payload = json.loads(response['Payload'].read())
        if response_payload['statusCode'] == 200:
            trending_hashtags = json.loads(response_payload['body'])
            st.write("Trending Hashtags:")
            for item in trending_hashtags:
                st.write(f"{item['hashtag']}: {item['count']} times")
        else:
            st.error(f"Error: {response_payload['body']}")
    except Exception as e:
        st.error(f"Error invoking Lambda function: {str(e)}")
