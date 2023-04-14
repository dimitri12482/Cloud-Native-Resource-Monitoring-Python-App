# SDK, which is used to create AWS resources in cloud
import boto3

ecr_client = boto3.client('ecr')
# Creating a respository
repository_name = "my_monitoring_app_image"
response = ecr_client.create_repository(repositoryName=repository_name)
# Repository URI, which used to deploy this application in kubernetes 
repository_uri = response['repository']['repositoryUri']
print(repository_uri)