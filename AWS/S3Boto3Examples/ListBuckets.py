import boto3
resource = boto3.resource('s3')

iterator = resource.buckets.all()

print("Listing all buckets")

for bucket in iterator:
    print("Bucket Name:"+bucket.name)
    s3_bucket = resource.Bucket(bucket.name)
    print("\n   Listing Bucket Files or Objects")
    for obj in s3_bucket.objects.all():
        print('{} | {} | {}'.format(obj.key, obj.size,obj.last_modified))
    #
    # for obj in s3_bucket.objects.all():
    #     #print("    "+obj.key)
    #     print(obj.name)
    # print("\nListing Bucket Files")
    # for obj in s3_bucket.objects.filter(Prefix="file"):
    #     print(bj.key)