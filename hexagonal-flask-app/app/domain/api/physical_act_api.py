from abc import ABC, abstractmethod

class PhysicalActApi(ABC):
    
    @abstractmethod
    def predict_physical_activities(self, data):
        pass