from sqlalchemy.orm import Session
from models import Usuario
 
class UserRepository:
    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(Usuario).filter(Usuario.cd_usuario == username).first()