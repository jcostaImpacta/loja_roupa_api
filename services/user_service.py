from sqlalchemy.orm import Session
import hashlib
from repositories.user_repository import UserRepository
from models import Usuario
 
class UserService:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()[:20]
 
    @staticmethod
    def validate_user(db: Session, username: str, password: str):
        user = UserRepository.get_user_by_username(db, username)
        if not user or user.cd_senha.strip() != UserService.hash_password(password):
            return None
        return user
    
    @staticmethod
    def create_user(db: Session, user: Usuario):
        user_db = UserRepository.get_user_by_username(db, user.cd_usuario)
        if user_db:
            return None
        user.cd_senha = UserService.hash_password(user.cd_senha)
        return UserRepository.create_user(db, user)
        
        
    
   
