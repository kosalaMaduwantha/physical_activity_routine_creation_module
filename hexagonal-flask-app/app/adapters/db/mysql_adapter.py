import sys
sys.path.append('/home/kosala/git-rep/physical_activity_routine_creation_module/hexagonal-flask-app/')
from app.domain.spi.db_spi import DBSPI, MetaDataException, NoDataFoundException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.adapters.db.conf_env import DB_STRING
from app.adapters.db.models import PhyActPrediction, User
from sqlalchemy.exc import IntegrityError
from app.adapters.db.db_table_creation import create_db_and_tables
from app.domain.api.dtos.models import phyActData
from sqlalchemy.sql import select
import logging

logger = logging.getLogger(__name__)

class MySQLAdapter(DBSPI):
    engine = create_engine(DB_STRING, echo=True)
        
    def __init__(self):
        self._session: Session = Session(bind=self.__class__.engine, autocommit=False)
        
    def get_prediction_data(self, user_id: str) -> list:
        query = select(PhyActPrediction).where(PhyActPrediction.uid == user_id)
        
        try:
            self._session.begin()
            result = self._session.execute(query).all()
            data = []
            for row in result:
                data.append(row[0])
            self._session.commit()
            if len(data) == 0:
                raise NoDataFoundException(f"Data not found for user id: {user_id}")
        
        except Exception as e:
            logger.error(e)
            if isinstance(e, NoDataFoundException):
                raise e
            else:
                raise MetaDataException(f"Error while fetching data: {e}")
            
        return data
    
    def save_prediction_data(self, data: phyActData) -> bool:
        outcome = False
        data_model = PhyActPrediction(**data.model_dump())
        
        try:
            self._session.begin()
            self._session.add(data_model)
            self._session.commit()
            outcome = True
        except IntegrityError as e:
            self._session.rollback()
            raise MetaDataException(f"Error while saving data: {e}")
        logger.info("Data saved successfully")
        
        return outcome
    
    def enter_user_tempory(self, user_id: str, username: str, 
                           password: str, email: str) -> bool:
        user_data_model = User(user_id=user_id, username=username, 
                               password=password, email=email)
        outcome = False
        try:
            self._session.begin()
            self._session.add(user_data_model)
            self._session.commit()
            outcome = True
        except IntegrityError as e:
            self._session.rollback()
            raise MetaDataException(f"Error while saving data: {e}")
        logger.info("Data saved successfully")
        
        return outcome
        
        
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
            
        