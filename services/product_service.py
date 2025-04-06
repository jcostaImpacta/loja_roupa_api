from sqlalchemy.orm import Session
from repositories.product_repository import ProductRepository
from schemas.produto_schema import FiltroProdutoSchema
from sqlalchemy import func
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
    def get_min_max_price(db: Session):
        result = db.query(
            func.min(Produtos.vl_produto).label("preco_min"),
            func.max(Produtos.vl_produto).label("preco_max")
    ).first()

        if result:
            return {"preco_min": result.preco_min, "preco_max": result.preco_max}
        else:
            return None
        return generos
    
    @staticmethod
    def get_colecoes(db: Session):
        colecoes = ProductRepository.get_colecoes(db)
        return colecoes