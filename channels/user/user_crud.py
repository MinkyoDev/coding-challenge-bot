from sqlalchemy.orm import Session

from db import models

def create_user(db_session: Session, 
                user_id: str, 
                name: str, 
                global_name: str, 
                git_username: str, 
                repository_name: str):
    existing_user = db_session.query(models.User).filter(models.User.git_username == git_username).first()
    if existing_user:
        return None
    db_user = models.User(id=user_id, 
                          name=name,
                          global_name=global_name,
                          git_username= git_username,
                          repository_name=repository_name,
                          use=True
                          )
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return db_user

def update_user(db_session: Session, 
                user_id: int, 
                name: str = None, 
                global_name: str = None, 
                git_username: str = None, 
                repository_name: str = None):
    db_user = db_session.query(models.User).filter(models.User.id == user_id).first()
    
    if db_user:
        if name is not None:
            db_user.name = name
        if global_name is not None:
            db_user.global_name = global_name
        if git_username is not None:
            db_user.git_username = git_username
        if repository_name is not None:
            db_user.repository_name = repository_name
        
        db_session.commit()
        db_session.refresh(db_user)
        return db_user
    else:
        raise Exception("User not found")
    
def get_user(db_session: Session, user_id: int):
    return db_session.query(models.User).filter(models.User.id == user_id).first()

def deactivate_user(db_session: Session, user_id: int):
    db_user = db_session.query(models.User).filter(models.User.id == user_id).first()
    
    if db_user:
        db_user.use = False
        
        db_session.commit()
        db_session.refresh(db_user)
        return db_user
    else:
        raise Exception("User not found")
    
def activate_user(db_session: Session, user_id: int):
    db_user = db_session.query(models.User).filter(models.User.id == user_id).first()
    
    if db_user:
        db_user.use = True
        
        db_session.commit()
        db_session.refresh(db_user)
        return db_user
    else:
        raise Exception("User not found")
    
def delete_user(db_session: Session, user_id: int):
    """
    지정된 사용자 ID를 가진 사용자 정보를 데이터베이스에서 삭제한다.

    Parameters:
    db_session (Session): SQLAlchemy 세션 객체
    user_id (int): 삭제할 사용자의 ID

    Returns:
    bool: 삭제 성공 여부
    """
    db_user = db_session.query(models.User).filter(models.User.id == user_id).first()
    
    if db_user:
        db_session.delete(db_user)
        db_session.commit()
        return True
    else:
        raise Exception("User not found")