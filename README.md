Social-Media-Hashtag-Trend-Analyzer

Introduction

The Social Media Hashtag Trend Analyzer Application is designed to help users compose posts with hashtags and analyze trending hashtags in real-time. This application leverages modern cloud technologies to process and store data, providing users with dynamic updates on trending topics.

Project Overview

The project consists of a Streamlit-based web application that allows users to:

1.	Compose and submit posts containing text and hashtags.
2.	Automatically process these posts using AWS Lambda.
3.	Store post data in DynamoDB.
4.	Retrieve and display trending hashtags based on the stored data.
5.	Ensure real-time updates of trending hashtags.
   
Technologies Used

•	Python: The primary programming language used for the backend and Streamlit application.
•	Streamlit: A web framework for creating interactive web applications.
•	AWS Lambda: A serverless compute service that runs code in response to events and automatically manages the underlying compute resources.
•	DynamoDB: A fast and flexible NoSQL database service provided by AWS.
•	boto3: The Amazon Web Services (AWS) SDK for Python, used to interact with AWS services.
•	dotenv: A Python library used to manage environment variables.

Usage

Prerequisites

•	Python 
•	AWS account with access to Lambda and DynamoDB services
•	Environment variables set for AWS credentials

Installation

1.	Clone the repository: clone the project repository from github to your local machine
2.	Install the required Python packages: pip install -r requirements.txt
3.	Create a .env file in the root directory and add your AWS credentials:
AWS_REGION_NAME=your_region_name
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

Running the Application

1.	Start the Streamlit application: streamlit run app.py
2.	Compose and submit a post:
o	Open the web application in your browser.
o	Write your post in the text area provided.
o	Click the "Post" button to submit your post.
3.	View trending hashtags:
o	Click the "Show Trending Hashtags" button to view the latest trending hashtags.

Lambda Functions

1.	ProcessPostFunction: This function is triggered when a post is submitted. It extracts hashtags from the post, stores the data in DynamoDB, and returns the updated trending hashtags.
2.	TrendingHashtagsFunction: This function retrieves and returns the trending hashtags based on the data stored in DynamoDB.
   
Updating AWS Lambda Functions

•	Package your Lambda function code and deploy it to AWS Lambda.
•	Ensure that the Lambda functions have the necessary permissions to access DynamoDB.

Conclusion

The Social Media Hashtag Trend Analyzer Application provides an efficient way to compose posts with hashtags and analyze trending topics in real-time. By leveraging AWS services and Streamlit, the application ensures scalability, reliability, and a user-friendly interface. Future enhancements could include more advanced analytics, user authentication, and integration with external social media platforms.

