# coding=utf-8
"""Storage helpers module."""

from google.cloud import storage

storage_client = None


def get_blob_as_string(bucket_name, blob_name):
    """Gets a blob in a bucket as a string.
    """
    global storage_client
    global context_key

    if storage_client is None:
        storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    return blob.download_as_string()
