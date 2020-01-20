import boto3 as boto3
from botocore.exceptions import ClientError


def store_file(file_name, file):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # Upload the file
    s3_client = boto3.resource('s3')
    try:
        response = s3_client.Bucket("a3-bucket-test").put_object(Key=file_name, Body=file)
    except ClientError as e:
        return False
    return True