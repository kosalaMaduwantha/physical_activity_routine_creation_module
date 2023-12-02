import sys
sys.path.append('/home/kosala/git-rep/physical_activity_routine_creation_module/hexagonal-flask-app/')
sys.path.append('/home/kosala/git-rep/physical_activity_routine_creation_module/hexagonal-flask-app/app/adapters/db/')
import os
import pickle
import numpy as np
from datetime import datetime
from app.domain.api.physical_act_api import PhysicalActApi
from app.domain.api.dtos.models import phyActData
from app.domain.services.encoder import GENDER, DISCOMFIRT_CHEST, \
    CURRENT_PHYSICAL_ACTIVITY_STATUS, FAMILY_HISTORY_HEART_DISEASE, CIGERETTE_CONSUMPTION
from app.domain.spi.db_spi import DBSPI
from app.adapters.db.mysql_adapter import MySQLAdapter
ROOT_DIR = "/home/kosala/git-rep/physical_activity_routine_creation_module/hexagonal-flask-app/"

class PhysicalActImpl(PhysicalActApi):
    
    def __init__(self, db_sp: DBSPI=None):
        self.db_sp = db_sp
        model_path = os.path.join(ROOT_DIR, "ML_models", "model.pkl")
        self.ml_model = pickle.load(open(model_path, "rb"))
        pass
    
    def predict_physical_activities(self, data: phyActData):
        preprocessed_data = self._preprocess_data(data)
        prediction = self.ml_model.predict(preprocessed_data)
        # update the class_ attribute of the data
        data.class_ = prediction[0]
        self._save_data_in_db(data)
        activity_list = self._select_activity_pool(prediction[0])
        return activity_list
    
    def get_physical_activities(self, user_id: str) -> list:
        data = self._get_prediction_data(user_id)
        
        max_date = datetime.min
        for row in data:
            if row.created_at > max_date:
                max_date = row.created_at
                data_latest = row
                
        activity_list = self._select_activity_pool(data_latest.class_)
        return activity_list
    
    def _preprocess_data(self, data: phyActData):
        
        encoded_data = {
            "age": data.age,
            "gender": GENDER[data.gender],
            "weight": data.weight,
            "height": data.height,
            "BloodPressure": data.blood_pressure,
            "cholestrol": data.cholestrol,
            "glucose": data.glucose,
            "diabetes": data.diabetes,
            "discomfirt_chest": DISCOMFIRT_CHEST[data.discomfirt_chest],
            "current_physical_activity_status": CURRENT_PHYSICAL_ACTIVITY_STATUS[data.current_physical_activity_status],
            "family_history_heart_disease": FAMILY_HISTORY_HEART_DISEASE[data.family_history_heart_disease],
            "cigerette_consumption": CIGERETTE_CONSUMPTION[data.cigerette_consumption]
            
        }
        numpy_array_data = np.array(list(encoded_data.values()))
        reshaped_data = numpy_array_data.reshape(1, 12)
        
        return reshaped_data
    
    def _select_activity_pool(self, class_: int) -> list:
        activity_pools = {
            1: ["Running", "Jogging", "Weight lifting", "Mountain Climbing", "Push ups", 
                "Hit ups", "swimming", "Cardio", "sports"],
            2: ["Running", "Jogging", "Weight lifting", "cycling moderate speed", "Yoga", 
                "Hit ups", "swimming", "Cardio", "Tai Chi"],
            3: ["Walking", "Jogging", "Cycling <10 mph leisure bicycling", "Yoga", 
                "Tai Chi", "Climbing stairs", "Rowing machine, moderate", "dancing"],
            4: ["Walking", "Slow Jogging", "Cycling <10 mph leisure bicycling", 
                "Stationary cycling very light", "Stationary cycling, light", 
                "Calisthenics light", "Yoga", "Tai Chi"]
        }
        
        return activity_pools[class_]
    
    def _save_data_in_db(self, data):
        self.db_sp.save_prediction_data(data)
        
    def _get_prediction_data(self, user_id: str):
        return self.db_sp.get_prediction_data(user_id)
    
if __name__ == "__main__":
    
    mysql_adapter = MySQLAdapter()
    phy_mod = PhysicalActImpl(mysql_adapter)
    
    # initialize data
    data = phyActData(
        age=67,
        gender="male",
        weight=160,
        height=5,
        blood_pressure=120,
        cholestrol=200,
        glucose=100,
        diabetes=1,
        discomfirt_chest="no",
        current_physical_activity_status="active",
        family_history_heart_disease="no",
        cigerette_consumption="no",
    )
    
    prediction = phy_mod.predict_physical_activities(data)
    print(prediction)
    
