from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    global_name = Column(String(255), unique=False, nullable=False)
    git_username = Column(String(255), unique=True, nullable=False)
    repository_name = Column(String(255), unique=False, nullable=False)
    created_at = Column(DateTime, default=func.now())
    use = Column(Boolean, nullable=False)
    
    commits = relationship("Commit", backref="commit_author")


class Commit(Base):
    __tablename__ = 'commits'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    author = Column(String(255), nullable=False)
    level = Column(String(255), nullable=False, default="unknown")
    title = Column(String(255), nullable=False, default="unknown")
    url = Column(String(255), nullable=False, default="unknown")
    message = Column(String(255), nullable=False, default="unknown")
    commit_date = Column(DateTime, default=func.now())
    