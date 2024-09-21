# Prerequisite is you should be authenticated to a google cloud project
# Either by gcloud init or gcloud auth application-default login

from google.cloud import storage
from google.cloud.exceptions import NotFound, Forbidden
 
def upload_to_gcs():
    try:
        storage_client = storage.Client()
    except Exception as e:
        print(f"Failed to create storage client: {e}")
        return
 
    bucket_name = input("Enter the unique bucket name to upload your file: ")
    
    try:
        bucket = storage_client.get_bucket(bucket_name)
    except NotFound:
        print(f"Bucket {bucket_name} not found. Please check the bucket name and your permissions.")
        return
    except Forbidden:
        print(f"Access to bucket {bucket_name} forbidden. Please check your permissions.")
        return
    except Exception as e:
        print(f"Error accessing bucket {bucket_name}: {e}")
        return
 
    blob_name = "mydata.json"
    blob = bucket.blob(blob_name)
 
    try:
        blob.upload_from_filename(blob_name)
        print(f"{blob_name} uploaded to Google Cloud Storage bucket {bucket_name}")
    except FileNotFoundError:
        print(f"File {blob_name} not found in the current directory.")
    except Exception as e:
        print(f"Error uploading file: {e}")
 
if __name__ == "__main__":
    upload_to_gcs()
