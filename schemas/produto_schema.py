from pydantic import BaseModel
from typing import Optional

class ProdutoSchema(BaseModel):
    id_produto: int
    dc_produto: str
    tp_categoria: int
    tp_publico: int
    tp_genero: int
    tp_colecao: int
    # dc_categoria: Optional[str]
    # dc_publico: Optional[str]
    # dc_genero: Optional[str]
    # dc_colecao: Optional[str]
    vl_produto: float
    qtd_produto: int
    fl_ativo: bool

    class Config:
        from_attributes = True

class FiltroProdutoSchema(BaseModel):
    categoria: Optional[str] = None
    publico: Optional[str] = None
    genero: Optional[str] = None
    colecao: Optional[str] = None

class CategoriaSchema(BaseModel):
    id_categoria: int
    dc_categoria: int