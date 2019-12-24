#*************************************************
# lambda_function.lambda_handler
# recuedas necesitas permisos sobre el lambda autoscaling:SetDesiredCapacity
#*************************************************
import boto3

def lambda_handler(event, context):
    client = boto3.client('autoscaling')
    response = client.set_desired_capacity(
        AutoScalingGroupName='eks-workers-111111111111551110119000011111',
        DesiredCapacity=4
    )