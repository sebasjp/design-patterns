import logging
import boto3
from creacionales.singleton.config import DynamoDBConfig
from creacionales.singleton.base_database import BaseDatabaseConnection, BaseDataBaseRepository

class AwsDynamoDBConnection(BaseDatabaseConnection):

    def __init__(self):
        self.connect()

    def connect(self):
        """Establish connection to DynamoDB"""
        try:
            self.client = boto3.resource("dynamodb", region_name=DynamoDBConfig.aws_region)            
            logging.info(f"Connected to dynamoDB")
        except Exception as e:
            logging.error(f"Error creating or connecting to Dynamo DB resources: {e}")
            raise e

    def close(self):
        self.client.close()
        
class AwsDynamoDBRepository(BaseDataBaseRepository):

    def __init__(self, table_name: str):
        self.conn = AwsDynamoDBConnection()
        self.table = self.conn.client.Table(table_name)

    def get_items(self, filter_by: dict):
        """Get items using filter_by."""

        scan_kwargs = {}
    
        if filter_by:
            scan_kwargs["FilterExpression"] = boto3.dynamodb.conditions.Attr(filter_by["key"]).eq(filter_by["value"])
    
        response = self.table.scan(**scan_kwargs)
        items = response.get("Items", [])
        last_evaluated_key = response.get("LastEvaluatedKey")

        while last_evaluated_key:
            scan_kwargs["ExclusiveStartKey"] = last_evaluated_key
            response = self.table.scan(**scan_kwargs)
            items.extend(response.get("Items", []))
            last_evaluated_key = response.get("LastEvaluatedKey")
    
        return items
    
    def put_item(self, item: dict):
        """Write a item to DynamoDB"""
        return self.table.put_item(Item=item)

    def delete_item(self, item_id: str, **kwargs):
        """Remove a item using item_id"""

        response = self.table.delete_item(Key={'PartitionKeyName': item_id})
        logging.info("Item deleted successfully.")