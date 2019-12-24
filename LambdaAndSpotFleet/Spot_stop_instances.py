#*************************************************
# lambda_function.lambda_handler
# recuedas necesitas permisos sobre el lambda startInstance y stopInstance
#*************************************************
import boto3

import json
region = 'us-east-1'

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.modify_spot_fleet_request( SpotFleetRequestId='sfr-1111111-1111-1111-1111-111111111111',
    TargetCapacity=0)
    return {
        'statusCode': 200,
        'body': json.dumps('stop your instances: ')
    }

