
import boto3

ec2 = boto3.client('ec2')       

TARGET_INSTANCE_ID = "i-053037aa05547dbe8"

def lambda_handler(event, context):
    response = ec2.describe_instances()
    stopped_instances = []
                                                             
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']

            if instance_id == TARGET_INSTANCE_ID and state == "running":
                ec2.stop_instances(InstanceIds=[instance_id])
                stopped_instances.append(instance_id)

    return {
        "status": "success",
        "stopped_instances": stopped_instances
    }
