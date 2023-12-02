from abc import ABC, abstractmethod
from app.domain.api.dtos.models import phyActData

class DBSPI(ABC):
    
    @abstractmethod
    def save_prediction_data(self, data: phyActData) -> bool:
        pass
    
    @abstractmethod
    def get_prediction_data(self, user_id: str) -> list:
        pass
    
class MetaDataException(Exception):
    def __init__(self, message):
        super().__init__(self.message)
        self.message = message
        
class NoDataFoundException(Exception):
    def __init__(self, message):
        super().__init__(self.message)
        self.message = message