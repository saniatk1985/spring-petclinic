#!/usr/bin/env python

import boto3

low_level_client = boto3.client('ec2')

keypairs = low_level_client.describe_key_pairs(KeyNames=['san1'], DryRun=False)

# SSH Key
keyname = keypairs['KeyPairs'][0]['KeyName']

sec_groups = low_level_client.describe_security_groups(GroupIds=['sg-87ebb4ea'], DryRun=False)

# Security group id
sec_group_id = sec_groups['SecurityGroups'][0]['GroupId']

subnets = low_level_client.describe_subnets(SubnetIds=['subnet-87b4deca'], DryRun=False)
subnet_id = subnets['Subnets'][0]['SubnetId']

# Go to high level
ec2 = boto3.resource('ec2')

# AMI ID
ami_id = 'ami-778ba99c'

instances = ec2.create_instances(
    ImageId=ami_id, InstanceType='t2.micro', MaxCount=2, MinCount=2, KeyName=keyname,
    NetworkInterfaces=[
        {'SubnetId': subnet_id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group_id]}
    ]
)
instances[0].create_tags(Tags=[{"Key": "Name", "Value": "App"}])
instances[0].wait_until_running()
instances[1].create_tags(Tags=[{"Key": "Name", "Value": "Mdb"}])
instances[1].wait_until_running()
print(instances[0].id)
print(instances[1].id)
