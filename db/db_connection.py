from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .db_config import DATABASE_URI
from .db_utils import create_database_if_not_exists, init_db, delete_all_table_contents


create_database_if_not_exists()

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

init_db(engine)
delete_all_table_contents(SessionLocal)

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
