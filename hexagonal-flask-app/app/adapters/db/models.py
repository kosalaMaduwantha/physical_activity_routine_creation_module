from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint, Float, Text
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import relationship, mapped_column
import json
import logging
from datetime import datetime 

logger = logging.getLogger(__name__)
FIELD_MAX_LENGTH = 255

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    
    user_id: Mapped[str] = mapped_column(String(FIELD_MAX_LENGTH), primary_key=True)
    username: Mapped[str] = mapped_column(String(FIELD_MAX_LENGTH), nullable=False)
    password: Mapped[str] = mapped_column(String(FIELD_MAX_LENGTH), nullable=False)
    email: Mapped[str] = mapped_column(String(FIELD_MAX_LENGTH), nullable=False)
    
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
    uid: Mapped[int] = mapped_column(String(FIELD_MAX_LENGTH), ForeignKey("user.user_id"))
    created_at: Mapped[str] = mapped_column(TIMESTAMP, nullable=False, default=datetime.now())
    
class Week(Base):
    __tablename__ = "week"
    
    week_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    week_no: Mapped[int] = mapped_column(Integer, nullable=True)
    month_of: Mapped[int] = mapped_column(Integer, nullable=True)
    year_of: Mapped[int] = mapped_column(Integer, nullable=True)
    
class Day(Base):
    __tablename__ = "day"
    
    day_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    day_no: Mapped[int] = mapped_column(Integer, nullable=True)
    week_no: Mapped[int] = mapped_column(Integer, ForeignKey("week.week_id"), nullable=True)

class ExerciseDataset(Base):
    __tablename__ = "exercise_dataset"
    
    activity: Mapped[str] = mapped_column(String(255), primary_key=True)  # Changed from Text to String(255)
    weight_130: Mapped[int] = mapped_column("130 lb", Integer, nullable=True)
    weight_155: Mapped[int] = mapped_column("155 lb", Integer, nullable=True)
    weight_180: Mapped[int] = mapped_column("180 lb", Integer, nullable=True)
    weight_205: Mapped[int] = mapped_column("205 lb", Integer, nullable=True)
    calories_per_kg: Mapped[float] = mapped_column("Calories per kg", Float, nullable=True)

class Routine(Base):
    __tablename__ = "routine"
    
    routine_act_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    activity: Mapped[str] = mapped_column(String(100), nullable=True)
    no_min: Mapped[int] = mapped_column(Integer, nullable=True)
    day_no: Mapped[int] = mapped_column(Integer, nullable=True)
    cus: Mapped[int] = mapped_column(Integer, nullable=True)

def init_db(engine):
    try:
        Base.metadata.create_all(engine)
        logger.info("Tables created")
    except Exception as e:
        logger.error("Error while creating tables")
        logger.error(e)
        raise e
    
