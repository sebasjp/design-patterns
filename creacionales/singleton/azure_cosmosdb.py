import logging
from azure.cosmos import CosmosClient
from creacionales.singleton.config import CosmosDBConfig
from creacionales.singleton.base_database import BaseDatabaseConnection, BaseDataBaseRepository

class AzureCosmosDBConnection(BaseDatabaseConnection):

    def __init__(self):
        self.connect()

    def connect(self):
        """Establish connection to Cosmos DB"""
        try:
            self.client = CosmosClient(CosmosDBConfig.endpoint, CosmosDBConfig.master_key)
            self.database = self.client.get_database_client(CosmosDBConfig.database)
            
            logging.info(f"Connected to databse '{CosmosDBConfig.database}'.")
        except Exception as e:
            logging.error(f"Error creating or connecting to Cosmos DB resources: {e}")
            raise e

    def close(self):
        self.client.close()
        
class AzureCosmosDBRepository(BaseDataBaseRepository):

    def __init__(self, container_name: str):
        self.conn = AzureCosmosDBConnection()
        self.container = self.conn.database.get_container_client(container_name)

    def get_items(self, filter_by: dict):
        """Get items using filter_by."""

        query = "SELECT * FROM c WHERE " + " AND ".join(
            [f"c.{key} = @{key}" for key in filter_by]
        )
        params = [
            {"name": f"@{key}", "value": value} 
            for key, value in filter_by.items()
        ]
        items = list(
            self.container.query_items(
                query=query,
                parameters=params,
                enable_cross_partition_query=True,
            )
        )
        return items
    
    def put_item(self, item: dict):
        """Write a item to cosmosDB"""
        return self.container.upsert_item(body=item)

    def delete_item(self, item_id: str, **kwargs):
        """Remove a item using item_id and partitionKey (if needed)"""

        partition_key = kwargs.get("partition_key")

        try:
            self.container.delete_item(item=item_id, partition_key=partition_key or item_id)
        except Exception as e:
            raise