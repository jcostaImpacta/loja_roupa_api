from pydantic import BaseModel
from datetime import datetime

class OrderResultSchema(BaseModel):
    cd_ordem: int
    cd_usuario: int
    vl_total: float
    qtd_total: int
    dt_venda: datetime

    class Config:
        from_attributes = True
