from abc import ABC, abstractmethod

class PhysicalActApi(ABC):
    
    @abstractmethod
    def predict_physical_activities(self, data):
        pass
    
    @abstractmethod
    def get_physical_activities(self, user_id):
        pass