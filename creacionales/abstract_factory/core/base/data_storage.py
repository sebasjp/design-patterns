from abc import ABC, abstractmethod


class StorageClient(ABC):

    @abstractmethod
    def list_files(self, **kwargs):
        pass

    @abstractmethod
    def upload_file(self, **kwargs):
        pass
        
    @abstractmethod
    def download_buffer_file(self, **kwargs):
        pass

    @abstractmethod
    def delete_file(self, **kwargs) -> None:
        pass