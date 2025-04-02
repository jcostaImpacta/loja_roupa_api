from sqlalchemy.orm import Session
from models import Produtos, Categoria, Publico, Genero, Colecao
from schemas.produto_schema import FiltroProdutoSchema
 
class ProductRepository:
    
    @staticmethod
    def get_categorias(db: Session):
        return db.query(Categoria)
    
    @staticmethod
    def get_publicos(db: Session):
        return db.query(Publico)
    
    @staticmethod
    def get_generos(db: Session):
        return db.query(Genero)
    
    @staticmethod
    def get_colecoes(db: Session):
        return db.query(Colecao)
    
    @staticmethod
    def get_products(db: Session, filtros: FiltroProdutoSchema):
        query = db.query(Produtos)
        
        if filtros.categoria is not None:
            query = query.filter(Produtos.tp_categoria == filtros.categoria)

        if filtros.publico is not None:
            query = query.filter(Produtos.tp_publico == filtros.publico)
        
        if filtros.genero is not None:
            query = query.filter(Produtos.tp_genero == filtros.genero)

        if filtros.colecao is not None:
            query = query.filter(Produtos.tp_colecao == filtros.colecao)

        if filtros.valor_min is not None:
            query = query.filter(Produtos.vl_produto >= filtros.valor_min)
        if filtros.valor_max is not None:
            query = query.filter(Produtos.vl_produto <= filtros.valor_max)

        return query.all()