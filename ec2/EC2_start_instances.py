#*************************************************
# lambda_function.lambda_handler
# recuedas necesitas permisos sobre el lambda startInstance y stopInstance
#*************************************************
import boto3

import json

region = 'us-east-1'

instances = ['i-0f41e5678d34ec40e','i-0f41e5678d34ec40e','i-0f41e5678d34ec40e']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)

    return {
        'statusCode': 200,
        'body': json.dumps('started your instances: ' + str(instances))
    }
