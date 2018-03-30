import google.cloud
from google.cloud import storage

storageClient = storage.Client()
if storageClient is not None:
    bucketName = input("Enter the bucket name to upload your file:")
    testBucket = storageClient.get_bucket(bucketName)
    if testBucket is not None:
        testBlob = testBucket.blob("mydata.json")
        if testBlob is not None:
            testBlob.upload_from_filename(jsonFileName)