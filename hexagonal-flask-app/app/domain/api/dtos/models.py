from pydantic import BaseModel

class phyActData(BaseModel):
    age: int
    gender: str
    weight: int
    height: int 
    blood_pressure: int
    cholestrol: int
    glucose: int
    diabetes: int
    discomfirt_chest: str
    current_physical_activity_status: str
    family_history_heart_disease: str
    cigerette_consumption: str
    class_: int = None
    

    
# 21,female,45.00,175,60,242,109,0,no,inactive,no,no,2,