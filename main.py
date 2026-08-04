import boto3
#AWS S3 File Manager
#Upload, list, and download files using Python and Boto3

print("AWS S3 Backup Manger")
print("                    ")

# Connect to AWS S3
s3 = boto3.client("s3")

# tekoaday3
BUCKET_NAME = "tekoaday3"

print("1. Upload file")
print("2. List files")
print("3. Download file")
print("4. Delete file")
print("5. Exit")

def upload_file():
    bucket_name = "tekoaday3"
    file_name = "test.txt"

    try:
        s3.upload_file(
            file_name,
            bucket_name,
            file_name
        )

        print("Upload successful!")

    except Exception as e:
        print("Upload failed:", e)


def list_files():
    bucket_name = "tekoaday3"

    try:
        response = s3.list_objects_v2(
            Bucket=bucket_name
        )

        if "Contents" in response:
            print("Files in bucket:")

            for file in response["Contents"]:
                print(file["Key"])

        else:
            print("No files found.")

    except Exception as e:
        print("Could not list files:", e)


def download_file():
    bucket_name = "tekoaday3"
    file_name = "test.txt"

    try:
        s3.download_file(
            bucket_name,
            file_name,
            file_name
        )

        print("Download successful!")

    except Exception as e:
        print("Download failed:", e)


def delete_file():
    try:
        bucket_name = "tekoaday3"
        file_name = "test.txt"

        s3.delete_object(
            Bucket= "tekoaday3",
            Key=file_name
        )

        print("Delete successful!")

    except Exception as e:
        print("Delete failed:", e)

      



upload_file()
list_files()
download_file()
        
      
        
      