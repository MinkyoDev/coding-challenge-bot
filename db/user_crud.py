from sqlalchemy.orm import Session
import models, db.database_connection as database_connection

def get_user(db_session: Session, user_id: int):
    return db_session.query(models.User).filter(models.User.id == user_id).first()

def create_user(db_session: Session, username: str, email: str):
    db_user = models.User(username=username, 
                          email=email,
                          )
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return db_user

# 사용 예제
# db = database_connection.SessionLocal()
# try:
#     user = create_user(db, "new_user", "new_user@example.com")
#     print(user.id, user.username, user.email)
# finally:
#     db.close()
