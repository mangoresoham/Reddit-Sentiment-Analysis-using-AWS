import base64
import json
import boto3

comprehend = boto3.client(service_name='comprehend', region_name='ap-south-1')

def lambda_handler(event, context):
    output = []
    
    for record in event['records']:
        try:
            # Decode base64-encoded data
            payload = base64.b64decode(record['data'])
            obj = json.loads(payload)
            
            # Extract text to be analyzed
            text_to_analyze = obj.get("text", "")
            
            # Perform sentiment analysis
            comp_response = comprehend.detect_sentiment(Text=text_to_analyze, LanguageCode='en')
            sentiment = comp_response.get("Sentiment", "UNKNOWN")
            
            # Add sentiment analysis result to the record
            obj["sentiment"] = sentiment
            
            # Encode the modified JSON object and prepare for Firehose
            output_record = {
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': base64.b64encode(json.dumps(obj, ensure_ascii=False).encode()).decode("utf-8") + '\n'
            }
            
            output.append(output_record)
        
        except Exception as e:
            # Handle errors gracefully
            output_record = {
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data']
            }
            output.append(output_record)
            print(f"Error processing record {record['recordId']}: {str(e)}")
    
    print(f"Successfully processed {len(event['records'])} records.")
    
    return {'records': output}
