class MYaStorageObject:

    import io
    import boto3

    KEY_ID = 'YCAJEF_D5aW3QysfttsyJW6rv'
    KEY_SECRET = 'YCPd-UNiM9VkD869kCG5xC74suoWH6YMZT3nME4j'

    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=KEY_ID,
        aws_secret_access_key=KEY_SECRET
    )


    def ListBuckets(self):
        try:
            bucket_response = self.s3.list_buckets()
            buckets = bucket_response["Buckets"]
            return buckets
        except Exception as e:
            return e

    def ListObjectsBuckets(self, B):
        try:
            for key in self.s3.list_objects(Bucket=B)['Contents']:
                print(key['Key'])
        except Exception as e:
            return e

    def upload_file(self, filepath, filename):
        bucket = 'sol'
        key = "FILES/IMAGES/" + filename
        try:
            self.s3.upload_file(filepath, bucket, key)
            return 'https://storage.yandexcloud.net/sol/FILES/IMAGES/' + filename
        except Exception as e:
            return e

    def UploadBinaryFile(self, bucket, folder, file_as_binary, file_name):
        file_as_binary = self.io.BytesIO(file_as_binary)
        key = folder + "/" + file_name
        try:
            self.s3.upload_fileobj(file_as_binary, bucket, key)
            return 'ok'
        except Exception as e:
            return e

    def DownloadFile(self):
        folder = 'SOFT'
        bucket = 'bucket-stop'
        file_name = 'AnyDesk.exe'
        key = folder + "/" + file_name
        try:
            with open(file_name, 'wb') as f:
                self.s3.download_fileobj(bucket, key, f)
            return 'ok'
        except Exception as e:
            return e

    def DeleteFile(self):
        try:
            self.s3.delete_object(Bucket='bt2', Key='bot_ava2.JPG')
            return 'ok'
        except Exception as e:
            return e

ClassS3 = MYaStorageObject()



