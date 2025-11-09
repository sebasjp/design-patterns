from abc import ABC, abstractmethod
from creacionales.singleton.base_singleton import SingletonMeta

class BaseDatabaseConnection(ABC, metaclass=SingletonMeta):
    """
    Clase abstracta para definir el contrato de conexión a base de datos.
    Todas las subclases heredan el comportamiento Singleton.
    """

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

class BaseDataBaseRepository(ABC):

    @abstractmethod
    def get_items(self, filter_by: dict):
        pass

    @abstractmethod
    def put_item(self, item: dict):
        pass

    @abstractmethod
    def delete_item(self, item_id: str, **kwargs):
        pass