from sqlalchemy.orm import Session
from repositories.product_repository import ProductRepository
 
class ProductService:
 
    @staticmethod
    def get_products(db: Session, categoria: int = None):
        return ProductRepository.get_products(db, categoria)
    
    @staticmethod
    def get_categorias(db: Session):
        categorias = ProductRepository.get_categorias(db)
        return categorias
    
    @staticmethod
    def get_publicos(db: Session):
        publicos = ProductRepository.get_publicos(db)
        return publicos
        
        
    
   