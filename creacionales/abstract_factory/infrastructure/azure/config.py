import os

class AzureConfig:
    cosmosdb_endpoint: str = os.getenv('COSMOS_ENDPOINT')
    cosmosdb_key: str = os.getenv('COSMOS_KEY')
    cosmosdb_database: str = os.getenv('COSMOS_DATABASE')
    ai_endpoint: str = os.getenv('AI_ENDPOINT')
    ai_api_key: str = os.getenv('AI_API_KEY')
    ai_api_version: str = os.getenv('AI_API_VERSION')
    ai_llm_model: str = os.getenv('AI_LLM_MODEL')
    ai_embedding_model: str = os.getenv('AI_EMBEDDING_MODEL')
    ai_embedding_dim: int = int(os.getenv('AI_EMBEDDING_DIM'))
    aisearch_endpoint: str = os.getenv('AISEARCH_ENDPOINT')
    aisearch_index_name: str = os.getenv('AISEARCH_INDEX_NAME')
    aisearch_key: str = os.getenv('AISEARCH_KEY')
    blob_storage_conn_string: str = os.getenv('BLOB_STORAGE_CONN_STRING')