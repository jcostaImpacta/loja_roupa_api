from pydantic import BaseModel
from datetime import datetime

class OrderSchema(BaseModel):
    cd_usuario: str
    vl_total_ordem: float
    qtd_total_produto: int

    class Config:
        from_attributes = True

class OrderResultSchema(BaseModel):
    id_ordem: int
    cd_usuario: str
    vl_total_ordem: float
    qtd_total_produto: int
    dt_ordem: datetime

    class Config:
        from_attributes = True
