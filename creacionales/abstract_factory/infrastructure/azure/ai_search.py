import logging as logger
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from creacionales.abstract_factory.core.base.vector_database import VectorSearchClient
from abstract_factory.infrastructure.azure.config import AzureConfig

    
class AzureAISearchClient(VectorSearchClient):

    def __init__(self):
        self.client = SearchClient(
            endpoint=AzureConfig.aisearch_endpoint, 
            index_name=AzureConfig.aisearch_index_name, 
            credential=AzureKeyCredential(AzureConfig.aisearch_key)
        )

    def search(self, input_text: str, top_k: int, vector: list[float]):

        search_results = self.client.search(
            search_text=input_text,
            top=top_k,
            vector_queries=[
                VectorizedQuery(
                    vector=vector, 
                    k_nearest_neighbors=top_k * 2, 
                    fields="vector"
                )
            ]
        )
        search_results = list(search_results)
        logger.info(f"# de documentos obtenidos: {len(search_results)}")

        return search_results
    
    def upload_docs(self, documents: list[dict]):
        """Upload documents to index AISearch
        {
            "chunk_id": chunk_id,
            "path": filename,
            "content": chunk,
            "vector": [...],
            ...
        }
        """
        logger.info("Subiendo embeddings a la vectorStore")
        self.client.upload_documents(documents=documents)

        return 'Documents indexed successfully'

    def delete_docs(self, delete_ids: list[dict]):
        """Eliminación de documentos del indice
        
        [{"chunk_id": "123"}]
        """
        # elimina los chunks del indice
        self.client.delete_documents(delete_ids)
        logger.info(f"Cantidad de chunks eliminados del indice: {len(delete_ids)}")

        return f'{len(delete_ids)} chunks deleted successfully'
