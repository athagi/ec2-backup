import json
import boto3
import datetime

# in 3 sec, enable to deregister max 4 amis.
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    if "generation" in event.keys():
        generation = event["generation"]
    instance_id = event["instance_id"]
    
    search_name = "backup_*_" + instance_id
    query = [
        {'Name': 'name', "Values": [search_name]}
    ]
    describe_images_result = ec2.describe_images(Filters=query)['Images']
    instance_list = sorted(describe_images_result, key=lambda images: images["ImageId"])
    
    removed_instance_list = instance_list[0: len(instance_list) - generation]
    removed_instance_amis = []
    for i in removed_instance_list:
        removed_instance_amis.append(i["ImageId"])
    
    flag = True
    for i in removed_instance_amis:
        response = ec2.deregister_image(ImageId= i)
        
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print("AMI " + i + " is removed")
        else:
            print("AMI " + i + " is not removed")
            flag = False
        
    if flag:
        return {
            'statusCode': 200
        }
    else:
        return {
            'statusCode': 400,
            'body': "some of ami is not removed"
        }
    