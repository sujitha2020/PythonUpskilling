import boto3
s3 = boto3.client('s3')
data = "gdsfghfdsfd\n fhghjgfhgfdh"
response = s3.put_object(Body=data,Bucket='zsdfghjkm', Key='sam.txt')
print(response)