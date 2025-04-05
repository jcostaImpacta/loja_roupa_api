from sqlalchemy.orm import Session
from repositories.product_repository import ProductRepository
from sqlalchemy import func
from models import Produtos
 
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
        
    def get_min_max_price(db: Session):
        result = db.query(
            func.min(Produtos.vl_produto).label("preco_min"),
            func.max(Produtos.vl_produto).label("preco_max")
    ).first()

        if result:
            return {"preco_min": result.preco_min, "preco_max": result.preco_max}
        else:
            return None
        
    
   