import sys
sys.path.append('/home/kosala/git-rep/physical_activity_routine_creation_module/hexagonal-flask-app/')
from app.domain.spi.db_spi import DBSPI, MetaDataException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.adapters.db.conf_env import DB_STRING
from app.adapters.db.models import PhyActPrediction, User
from sqlalchemy.exc import IntegrityError
from app.adapters.db.db_table_creation import create_db_and_tables
from app.domain.api.dtos.models import phyActData
import logging

logger = logging.getLogger(__name__)

class MySQLAdapter(DBSPI):
    engine = create_engine(DB_STRING, echo=True)
        
    def __init__(self):
        self._session: Session = Session(bind=self.__class__.engine, autocommit=False)
    
    def save_prediction_data(self, data: phyActData):
        data_model = PhyActPrediction(**data.model_dump())
        
        try:
            self._session.begin()
            self._session.add(data_model)
            self._session.commit()
        except IntegrityError as e:
            self._session.rollback()
            raise MetaDataException(f"Error while saving data: {e}")
        logger.info("Data saved successfully")
        
        return True
    
    def enter_user_tempory(self, user_id: str, username: str, 
                           password: str, email: str):
        user_data_model = User(user_id=user_id, username=username, 
                               password=password, email=email)
        try:
            self._session.begin()
            self._session.add(user_data_model)
            self._session.commit()
        except IntegrityError as e:
            self._session.rollback()
            raise MetaDataException(f"Error while saving data: {e}")
        logger.info("Data saved successfully")
        
        return True
        
        
if __name__ == "__main__":
    create_db_and_tables()
    mysql_adapter = MySQLAdapter()
    
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
        cigerette_consumption="no"
    )
    
    outcome = mysql_adapter.save_prediction_data(data)
    print(outcome)
            
        