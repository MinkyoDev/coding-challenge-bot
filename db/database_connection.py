from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import mysql.connector
from .database_config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DATABASE, DATABASE_URI
from .models import Base

def create_database_if_not_exists():
    try:
        connection = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DATABASE}')
            cursor.close()
        connection.close()
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

create_database_if_not_exists()

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
