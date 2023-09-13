import boto3
s3 = boto3.client('s3')
response = s3.get_object(Bucket='zsdfghjkm', Key='readme.txt')
data = response['Body'].read()
print(data)