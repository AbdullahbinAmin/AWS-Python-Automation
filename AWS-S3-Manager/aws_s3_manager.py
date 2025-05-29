import boto3
import botocore

# Step 1: Connect to S3
s3 = boto3.client('s3')
region = 'eu-north-1'

# Step 2: Create a unique bucket
bucket_name = 'abdullah-aws-bucket-2025-05-29-001'
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})

# Step 3: Upload a file
local_file_path = 'local_file.txt'
object_key = 'remote_file.txt'
s3.upload_file(local_file_path, bucket_name, object_key)

# Step 4: Download the same file
s3.download_file(bucket_name, object_key, local_file_path)

# Step 5: Enable versioning
s3.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={
        'Status': 'Enabled'
    }
)

# Step 6: List all file versions
response = s3.list_object_versions(Bucket=bucket_name)
for version in response.get('Versions', []):
    print(f"Object Key: {version['Key']}, Version ID: {version['VersionId']}")
