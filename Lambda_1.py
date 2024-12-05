import praw
import json
import uuid
import boto3

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id='*****************',
    client_secret="***************",
    user_agent="**************",  # It's just name, you can keep it simple like my_app
    username="****************",
    password="**************",
)

# Initialize the Kinesis Data Firehose client
firehose = boto3.client('firehose')

# Lambda handler function
def lambda_handler(event, context):
    # Parameters for fetching comments (subreddit name, limit)
    subreddit_name = event.get('subreddit', 'AskReddit')  # Default subreddit: AskReddit
    limit = event.get('limit', 10)  # Default limit: 10 comments
    
    # Fetch comments from Reddit API
    subreddit = reddit.subreddit(subreddit_name)
    comments = subreddit.comments(limit=limit)
    
    # Prepare records to send to Firehose
    records = []
    for comment in comments:
        comment_data = {
            'comment_id': str(uuid.uuid4()),
            'text': comment.body,
            'author': comment.author.name,
            'subreddit': subreddit_name,
            'timestamp': str(comment.created_utc)  # Convert timestamp to string
        }
        # Convert the comment data to a JSON string
        comment_json = json.dumps(comment_data, ensure_ascii=False)
        # Prepare the record for Firehose
        record = {
            'Data': comment_json.encode('utf-8')  # Encode the JSON string as bytes
        }
        records.append(record)
    
    # Send records to Firehose
    #firehose_name = 'kinesis-learn-python'  # Name of your Firehose delivery stream
    #firehose_name= 'kinesis-sentiment-analysis' 
    firehose_name= 'Kinesis-comment_Id'
    response = firehose.put_record_batch(
        DeliveryStreamName=firehose_name,
        Records=records
    )
    
    # Log the response from Firehose
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data sent to Firehose successfully'})
    }
