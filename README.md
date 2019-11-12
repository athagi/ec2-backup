# ec2-backup
aws cloudformation create-stack --stack-name hagita-test --template-body file://create-ec2.yml --parameters ParameterKey=InstanceKeyName,ParameterValue={{ KEY_NAME }},UsePreviousValue=true,ResolvedValue=string ParameterKey=MyIP,ParameterValue={{ MY_IP }}/32,UsePreviousValue=true,ResolvedValue=string
