# ec2-backup

## usage
Create maintenace window in SSM
```
aws cloudformation create-stack --template-body file://backup-ec2.yml --stack-name {{ STACK_NAME }} --capabilities CAPABILITY_NAMED_IAM
```

Create test instance
```
aws cloudformation create-stack --stack-name {{ STACK_NAME }} --template-body file://create-ec2.yml --parameters ParameterKey=InstanceKeyName,ParameterValue={{ KEY_NAME }},UsePreviousValue=true,ResolvedValue=string ParameterKey=MyIP,ParameterValue={{ MY_IP }}/32,UsePreviousValue=true,ResolvedValue=string
```