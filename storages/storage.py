from abc import ABC, abstractmethod
from serializers.serializer import Serializer

class Storage(ABC):
    @abstractmethod
    def __init__(self, path: str, serializer: Serializer):
        pass

    @abstractmethod
    def get_data_from_storage(self):
        return []

    @abstractmethod
    def update_storage(self, records: []):
        pass
