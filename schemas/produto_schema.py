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
    categoria: Optional[str] = None
    publico: Optional[str] = None
    genero: Optional[str] = None
    colecao: Optional[str] = None
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