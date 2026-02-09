import logging
import time
from openai import AzureOpenAI
from abstract_factory.core.base.llm import LLMClient
from abstract_factory.infrastructure.azure.config import AzureConfig


class AzureLLMClient(LLMClient):

    def __init__(self, model: str):
        self.client = AzureOpenAI(
            azure_endpoint=AzureConfig.ai_endpoint,
            api_key=AzureConfig.ai_api_key,
            api_version=AzureConfig.ai_api_version
        )
        self.model = model
        self.tokens_usage_llm = {}

    def invoke(self, system_prompt: str, input_text: str):
        """Performs the chat_completion request and returrns the choices[0].message.content and token_input and token_output used in the request."""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text},
        ]
        attempts = 0
        while attempts < self.max_retries:
            response = self.client.chat.completions.create(
                model=self.model, messages=messages
            )
            if self._handle_response(response=response):
                token_input = response.usage.prompt_tokens
                token_output = response.usage.completion_tokens
                logging.info(f"token_input={token_input} - token_output={token_output}")                
                self.save_usage(token_input, token_output)
                
                return response.choices[0].message.content
            attempts += 1
            time.sleep(2**attempts)
        raise Exception(f"Failed after {self.max_retries} retries.")

    def _handle_response(self, response):
        """Check if 'choices' exists and is not empty"""
        if not response.choices:
            return False
        choice = response.choices[0]
        if choice.finish_reason not in ["stop", "lenght"]:
            return False

        return True

    def save_usage(self, tokens_input: int, tokens_output: int):

        if self.model not in self.tokens_usage_llm:
            self.tokens_usage_llm[self.model] = {"input_tokens": 0, "output_tokens": 0}

        self.tokens_usage_llm[self.model]["input_tokens"] += tokens_input
        self.tokens_usage_llm[self.model]["output_tokens"] += tokens_output