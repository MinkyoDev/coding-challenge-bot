from sqlalchemy.orm import Session
import datetime

from db import models

    
def get_user(db_session: Session, user_id: int):
    return db_session.query(models.User).filter(models.User.id == user_id).first()

def create_commit(db_session: Session, 
                  user_id: int, 
                  level: str,
                  title: str,
                  url: str,
                  message: str, 
                  commit_date: datetime
                  ):
    """
    새로운 커밋을 데이터베이스에 추가한다.

    Parameters:
    db_session (Session): SQLAlchemy 세션 객체
    user_id (int): 커밋을 생성하는 사용자의 ID
    message (str): 커밋 메시지
    commit_date (datetime): 커밋 날짜

    Returns:
    Commit: 생성된 커밋 객체
    """
    db_commit = models.Commit(user_id=user_id, 
                            #   level=
                            #   title=
                            #   url=
                              message=message, 
                              commit_date=commit_date
                              )
    db_session.add(db_commit)
    db_session.commit()
    db_session.refresh(db_commit)
    return db_commit

def get_commits_by_user(db_session: Session, user_id: int):
    """
    특정 사용자에 의해 생성된 모든 커밋을 조회한다.

    Parameters:
    db_session (Session): SQLAlchemy 세션 객체
    user_id (int): 커밋을 조회할 사용자의 ID

    Returns:
    List[Commit]: 해당 사용자에 의해 생성된 모든 커밋의 리스트
    """
    return db_session.query(models.Commit).filter(models.Commit.user_id == user_id).all()