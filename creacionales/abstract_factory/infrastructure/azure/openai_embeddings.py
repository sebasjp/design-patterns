from openai import AzureOpenAI
from abstract_factory.core.base.embeddings import VectorClient
from abstract_factory.infrastructure.azure.config import AzureConfig


class AzureVectorClient(VectorClient):

    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=AzureConfig.ai_endpoint,
            azure_deployment=AzureConfig.ai_embedding_model,
            api_version=AzureConfig.ai_api_version,
            api_key=AzureConfig.ai_api_key,
        )
        self.tokens = 0
        self.model = AzureConfig.ai_embedding_model
    
    def invoke(self, input_text: str):
        response = self.client.embeddings.create(
            input=input_text,
            model=self.model,
            dimensions=AzureConfig.ai_embedding_dim
        )
        self.save_usage(response.usage.total_tokens)
        response_emb = [dict(i) for i in response.data]
        return response_emb[0]["embedding"]

    def save_usage(self, tokens_usage: int):
        self.tokens += tokens_usage