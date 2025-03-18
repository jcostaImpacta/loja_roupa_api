from sqlalchemy.orm import Session
from models import Produtos, Categoria
 
class ProductRepository:
    @staticmethod
    def get_products(db: Session):
        return db.query(Produtos)
    
    @staticmethod
    def get_categorias(db: Session):
        return db.query(Categoria)