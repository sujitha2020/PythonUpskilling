import boto3


region ='eu-west-3'
# bucket_name = 'zsdfghjk'
bucket_name = 'zsdfghjkm'
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket=bucket_name)
# s3_client = boto3.client('s3', region_name=region)
# location = {'LocationConstraint': region}
# s3_client.create_bucket(Bucket=bucket_name,
#                                     CreateBucketConfiguration=location)

#print(response)