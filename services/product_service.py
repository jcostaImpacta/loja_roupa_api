from sqlalchemy.orm import Session
from repositories.product_repository import ProductRepository
from schemas.produto_schema import FiltroProdutoSchema
from models import Produtos
 
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
        
    @staticmethod
    def get_generos(db: Session):
        generos = ProductRepository.get_generos(db)
        return generos

    
    @staticmethod
    def get_min_max_price(db: Session):
        result = ProductRepository.get_min_max_price(db)

        result["preco_min"] = result["preco_min"] or 0
        result["preco_max"] = result["preco_max"] or 300
        return result
        
    
    @staticmethod
    def get_colecoes(db: Session):
        colecoes = ProductRepository.get_colecoes(db)
        return colecoes