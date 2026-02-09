from abc import ABC, abstractmethod


class VectorClient(ABC):

    @abstractmethod
    def invoke(self, input_text: str):
        pass

    @abstractmethod
    def save_usage(self, tokens_usage: int):
        pass