import boto3

BUCKET_NAME = "zsdfghjkm"

s3_resource = boto3.resource('s3')

s3_object = s3_resource.Object(BUCKET_NAME, 'sample.json')

s3_object.download_file('downloaded.json')

print("File has been downloaded")