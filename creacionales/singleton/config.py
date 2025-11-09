import os

class CosmosDBConfig:
    endpoint: str = os.getenv('COSMOS_ENDPOINT')
    master_key: str = os.getenv('COSMOS_KEY')
    database: str = os.getenv('COSMOS_DATABASE')

class DynamoDBConfig:
    aws_region: str = os.getenv('AWS_REGION')