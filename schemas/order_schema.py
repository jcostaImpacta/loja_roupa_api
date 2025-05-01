from pydantic import BaseModel
from datetime import datetime

class OrderSchema(BaseModel):
    cd_usuario: int
    vl_total: float
    qtd_total: int

    model_config = {
        "from_attributes": True
    }

class OrderResultSchema(BaseModel):
    cd_ordem: int
    cd_usuario: int
    vl_total: float
    qtd_total: int
    dt_venda: datetime

    model_config = {
        "from_attributes": True
    }
