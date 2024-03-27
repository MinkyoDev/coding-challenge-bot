from sqlalchemy import Column, BigInteger, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    global_name = Column(String(255), unique=False, nullable=False)
    git_username = Column(String(255), unique=False, nullable=False)
    repository_name = Column(String(255), unique=False, nullable=False)
    created_at = Column(DateTime, default=func.now())
    use = Column(Boolean, nullable=False)
