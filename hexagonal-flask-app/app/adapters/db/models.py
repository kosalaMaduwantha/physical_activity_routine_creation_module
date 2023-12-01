from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import relationship, mapped_column
import json
import logging

logger = logging.getLogger(__name__)
FIELD_MAX_LENGTH = 255

class Base(DeclarativeBase):
    pass

class PhyActPrediction(Base):
    __tablename__ = "phy_act_prediction"
    
    id: Mapped[str] = mapped_column(Integer, primary_key=True, autoincrement=True)
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(FIELD_MAX_LENGTH))
    weight: Mapped[int] = mapped_column(Integer)
    height: Mapped[int] = mapped_column(Integer)
    blood_pressure: Mapped[int] = mapped_column(Integer)
    cholestrol: Mapped[int] = mapped_column(Integer)
    glucose: Mapped[int] = mapped_column(Integer)
    diabetes: Mapped[int] = mapped_column(Integer)
    discomfirt_chest: Mapped[str] = mapped_column(String(FIELD_MAX_LENGTH))
    current_physical_activity_status: Mapped[str] = mapped_column(String(FIELD_MAX_LENGTH))
    family_history_heart_disease: Mapped[str] = mapped_column(String(FIELD_MAX_LENGTH))
    cigerette_consumption: Mapped[str] = mapped_column(String(FIELD_MAX_LENGTH))
    class_: Mapped[int] = mapped_column(Integer, nullable=True)
    
def init_db(engine):
    try:
        Base.metadata.create_all(engine)
        logger.info("Tables created")
    except Exception as e:
        logger.error("Error while creating tables")
        logger.error(e)
        raise e
    
