from abc import ABC, abstractmethod
from app.domain.api.dtos.models import phyActData, RoutineRecData

class PhysicalActApi(ABC):
    
    @abstractmethod
    def predict_physical_activities(self, data: phyActData):
        pass
    
    @abstractmethod
    def get_physical_activities(self, user_id: str):
        pass
    
    @abstractmethod
    def create_routine(self, user_id: str, data: RoutineRecData):
        pass