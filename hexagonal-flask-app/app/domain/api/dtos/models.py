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
    uid: int = None
    class_: int = None
    
class Activity(BaseModel):
    name: str
    calories: int
    
class RoutineRecData(BaseModel):
    activities: list[Activity]
    target_calories: int
    no_hours: int