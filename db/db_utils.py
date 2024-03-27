from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import mysql.connector

from .db_config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DATABASE
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

def init_db(engine):
    Base.metadata.create_all(bind=engine)

def drop_all_tables(engine):
    try:
        Base.metadata.drop_all(bind=engine)
        print("모든 테이블이 성공적으로 삭제되었습니다.")
    except SQLAlchemyError as e:
        print(f"테이블 삭제 중 오류 발생: {e}")

def delete_all_table_contents(SessionLocal):
    db = SessionLocal()
    try:
        for table_name in Base.metadata.tables.keys():
            db.execute(text(f'DELETE FROM {table_name}'))
        db.commit()
        print("모든 테이블의 내용이 성공적으로 삭제되었습니다.")
    except Exception as e:
        db.rollback()
        print(f"데이터 삭제 중 오류 발생: {e}")
    finally:
        db.close()