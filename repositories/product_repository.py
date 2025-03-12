from sqlalchemy.orm import Session
from models import Produtos
 
class ProductRepository:
    @staticmethod
    def get_products(db: Session):
        return db.query(Produtos)