from sqlalchemy.orm import Session
import hashlib
from repositories.product_repository import ProductRepository
from models import Usuario
 
class ProductService:
 
    @staticmethod
    def get_products(db: Session):
        products = ProductRepository.get_products(db)
        return products
    
    # @staticmethod
    # def create_user(db: Session, user: Usuario):
    #     user_db = UserRepository.get_user_by_username(db, user.cd_usuario)
    #     if user_db:
    #         return None
    #     user.cd_senha = UserService.hash_password(user.cd_senha)
    #     return UserRepository.create_user(db, user)
        
        
    
   