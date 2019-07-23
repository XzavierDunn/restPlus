import os
import boto3

s3 = boto3.resource('s3')

def upload_images():
    for root, dirs, files in os.walk('images'):
        for file in files:
            s3.meta.client.upload_file(os.path.join(root, file), 'xdtest-bucket', 'images')


def download_images():
    s3.meta.client.download_file('test-bucket-xd', 'images', 'images')


upload_images()
