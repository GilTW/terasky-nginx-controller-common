import boto3
from botocore.errorfactory import ClientError

s3_client = boto3.client("s3")
s3 = boto3.resource('s3')


def get_file_content(bucket, key, encoding="utf-8"):
    result = None

    try:
        content = s3_client.get_object(Bucket=bucket, Key=key)

        result = content['Body'].read().decode(encoding)
    except ClientError as ex:
        if "NoSuchKey" not in str(ex):
            raise ex

    return result


def save_file_content(bucket, key, file_content, encoding="utf-8", **extra_agrs):
    body = file_content

    if isinstance(body, str):
        body = body.encode(encoding=encoding)

    return s3_client.put_object(Bucket=bucket, Key=key, Body=body, **extra_agrs)


def download_file(bucket, key, file_path):
    s3.meta.client.download_file(bucket, key, file_path)
