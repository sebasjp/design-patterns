from abc import ABC, abstractmethod

class NoSqlConnection(ABC):

    @abstractmethod
    def connect(self):
        pass


class NoSqlRepository(ABC):

    @abstractmethod
    def get_items(self, filter_by: dict):
        pass

    @abstractmethod
    def put_item(self, item: dict):
        pass

    @abstractmethod
    def delete_item(self, item_id: str, **kwargs):
        pass