from sqlalchemy.orm import Session
from repositories.product_repository import ProductRepository
from schemas.produto_schema import FiltroProdutoSchema
 
class ProductService:
 
    @staticmethod
    def get_products(db: Session, filtros: FiltroProdutoSchema):
        return ProductRepository.get_products(db, filtros)
    
    @staticmethod
    def get_categorias(db: Session):
        categorias = ProductRepository.get_categorias(db)
        return categorias
    
    @staticmethod
    def get_publicos(db: Session):
        publicos = ProductRepository.get_publicos(db)
        return publicos
        
        
    
   