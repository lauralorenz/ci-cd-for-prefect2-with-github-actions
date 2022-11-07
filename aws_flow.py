from prefect import flow, get_run_logger
from prefect_aws import AwsCredentials
from prefect_aws.s3 import s3_upload
from prefect.filesystems import S3

@flow
def hello_upload_flow():

    s3_block = S3.load("demo-bucket")

    aws_credentials = AwsCredentials(
        aws_access_key_id=s3_block.aws_access_key_id.get_secret_value(),
        aws_secret_access_key=s3_block.aws_secret_access_key.get_secret_value()
    )

    with open("hello.md", "rb") as file:
        key = s3_upload(
            bucket=s3_block.bucket_path,
            key="hello.md",
            data=file.read(),
            aws_credentials=aws_credentials,
        )

if __name__ == "__main__":
    hello_upload_flow()

