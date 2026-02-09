import io
import os
from azure.storage.blob import BlobServiceClient
from abstract_factory.core.base.data_storage import StorageClient
from abstract_factory.infrastructure.azure.config import AzureConfig


class BlobStorageClient(StorageClient):

    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(AzureConfig.blob_storage_conn_string)

    def list_files(self, container_name: str):

        container_client = self.client.get_container_client(container_name)
        try:
            return [blob.name for blob in container_client.list_blobs()]
        except Exception as e:
            raise

    def upload_file(self, file_path: str, container: str, blob_name: str=None):

        try:            
            if not blob_name:
                blob_name = os.path.basename(file_path)
            blob_client = self.client.get_blob_client(container=container, blob=blob_name)
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
        except Exception as e:
            raise
        
    def download_buffer_file(self, container_name: str, blob_name: str):

        container_client = self.client.get_container_client(container_name)

        # Crear un cliente para el blob
        blob_client = container_client.get_blob_client(blob_name)

        if not blob_client.exists():
            raise FileNotFoundError(f"El blob '{blob_name}' no existe en el contenedor '{container_name}'.")
        
        # Descargar el blob a un buffer en memoria
        download_stream = blob_client.download_blob()
        buffer_data = io.BytesIO(download_stream.readall())

        return buffer_data

    def delete_file(self, container_name: str, blob_name: str):
        try:
            blob_client = self.client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.delete_blob()
        except Exception as e:
            raise