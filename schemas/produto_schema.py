from pydantic import BaseModel
from typing import Optional

class ProdutoSchema(BaseModel):
    id_produto: int
    dc_produto: str
    tp_categoria: int
    tp_publico: int
    tp_genero: int
    tp_colecao: int
    vl_produto: float
    qtd_produto: int
    fl_ativo: bool

    class Config:
        from_attributes = True

class FiltroProdutoSchema(BaseModel):
    categoria: Optional[int] = None
    publico: Optional[int] = None
    genero: Optional[int] = None
    colecao: Optional[int] = None
    valor_min: Optional[float] = None
    valor_max: Optional[float] = None

class CategoriaSchema(BaseModel):
    id_categoria: int
    dc_categoria: str

class PublicoSchema(BaseModel):
    id_publico: int
    dc_publico: str

class GeneroSchema(BaseModel):
    id_genero: int
    dc_genero: str

class ColecaoSchema(BaseModel):
    id_colecao: int
    dc_colecao: str


class MinMaxPriceSchema(BaseModel):
    preco_min: float
    preco_max: float
    