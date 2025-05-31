def handler(event, context):
    print("Lambda function triggered!")
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
