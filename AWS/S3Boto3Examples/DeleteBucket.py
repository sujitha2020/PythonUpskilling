import boto3


region ='eu-west-3'
bucket_name = 'zsdfghjk'
s3_client = boto3.client('s3')
s3_client.delete_bucket(Bucket=bucket_name)

print("S3 Bucket has been deleted")