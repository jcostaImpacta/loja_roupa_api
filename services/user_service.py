from sqlalchemy.orm import Session
import hashlib
from repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()[:20]

    @staticmethod
    def validate_user(db: Session, username: str, password: str):
        user = UserRepository.get_user_by_username(db, username)
        senhaHash = UserService.hash_password(password)
        if not user or user.cd_senha.strip() != senhaHash:
            return None
        return user