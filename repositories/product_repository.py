from sqlalchemy.orm import Session
from models import Produtos, Categoria, Publico, Genero, Colecao
from schemas.produto_schema import FiltroProdutoSchema
from sqlalchemy import func
from collections import namedtuple
 
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
    
    @staticmethod
    def get_min_max_price(db: Session):
        result = (
        db.query(
            func.min(Produtos.vl_produto).label("preco_min"),
            func.max(Produtos.vl_produto).label("preco_max")
        )
        .first()
        )

        FaixaPreco = namedtuple("FaixaPreco", ["preco_min", "preco_max"])

        if result is None or result[0] is None and result[1] is None:
                faixa = FaixaPreco(None, None)
        else:
            faixa = FaixaPreco(*result)

        return {
            "preco_min": faixa.preco_min,
            "preco_max": faixa.preco_max
    }

    @staticmethod
    def update_product(db: Session, produto: Produtos):

        produto_existente = db.query(Produtos).filter_by(id_produto=produto.id_produto).first()
        
        if not produto_existente:
            raise Exception("Produto não encontrado")
        
        produto_existente.qtd_produto = produto.qtd_produto

        db.commit()
        db.refresh(produto_existente)

        return produto_existente