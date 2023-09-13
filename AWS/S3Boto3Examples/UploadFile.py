import boto3




BUCKET_NAME =   "zsdfghjkm"

s3_client = boto3.client('s3')

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print("{} has been uploaded to {} bucket".format(file_name, BUCKET_NAME))



upload_files("file.txt", BUCKET_NAME)