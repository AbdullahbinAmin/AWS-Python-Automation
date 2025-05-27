import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

print("S3 Buckets List:")
for bucket in response['Buckets']:
    print(f' → {bucket["Name"]}')