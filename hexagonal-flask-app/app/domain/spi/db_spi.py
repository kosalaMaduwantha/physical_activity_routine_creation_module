from abc import ABC, abstractmethod

class DBSPI(ABC):
    
    @abstractmethod
    def save_prediction_data(self, data):
        pass
    
class MetaDataException(Exception):
    def __init__(self, message):
        super().__init__(self.message)
        self.message = message