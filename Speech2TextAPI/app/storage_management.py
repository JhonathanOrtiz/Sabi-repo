from google.cloud import storage
import requests
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "app/All-project-services-05f5490b9fae.json"

client = storage.Client()

def upload_and_get_uri(content, bucket_name, filename):
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_string(content)
    return "gs://" + bucket_name + '/' + filename

def delete_blob(bucket, filename):
    bucket = client.get_bucket(bucket)
    blob = bucket.blob(filename)
    blob.delete()