# ec2-backup

## usage
Create bucket
```
aws cloudformation deploy --template-file create-s3.yml --stack-name {{ STACK_NAME }} --parameter-overrides S3BucketName={{ BUCKET_NAME }}
```

Upload s3 and create yaml from template
```
aws cloudformation package --template-file backup-ec2.template --s3-bucket {{ BUCKET_NAME }} --output-template-file backup-ec2.yml 
```

Create maintenace window in SSM
```
aws cloudformation deploy --template-file backup-ec2.yml --stack-name {{ BUCKET_NAME }} --capabilities CAPABILITY_NAMED_IAM --parameter-overrides BackupGeneration=3
```

Create test instance
```
aws cloudformation deploy --template-file create-ec2.yml --stack-name {{ STACK_NAME }} --parameter-overrides InstanceKeyName={{ KEY_NAME }} MyIP={{ MY_IP }}/32
```
