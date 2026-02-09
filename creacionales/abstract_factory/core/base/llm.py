from abc import ABC, abstractmethod


class LLMClient(ABC):

    @abstractmethod
    def invoke(self, system_prompt: str, input_text: str):
        pass

    @abstractmethod
    def save_usage(self, tokens_input: int, tokens_output: int):
        pass