from abc import ABC, abstractmethod


class VectorSearchClient(ABC):

    @abstractmethod
    def search(self, input_text: str, top_k: int, vector: list[float]):
        pass

    @abstractmethod
    def upload_docs(self, documents: list[dict]):
        pass

    @abstractmethod
    def delete_docs(self, delete_ids: list[dict]):
        pass