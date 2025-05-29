from pydantic import BaseModel
from datetime import datetime
from models import Produtos

class OrderSchema(BaseModel):
    cd_usuario: str
    vl_total_ordem: float
    qtd_total_produto: int
    lista_produtos: list[Produtos]

    class Config:
        from_attributes = True

class OrdemProdutoSchema(BaseModel):
    id_ordem: int
    id_produto: int
    qtd_produto: int
    vl_produto_venda: float

class OrderResultSchema(BaseModel):
    id_ordem: int
    cd_usuario: str
    vl_total_ordem: float
    qtd_total_produto: int
    dt_ordem: datetime

    class Config:
        from_attributes = True
