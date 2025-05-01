from datetime import datetime, timezone
from schemas.order_schema import OrderSchema
from schemas.order_result_schema import OrderResultSchema  
from repositories.order_repository import criar_ordem
from models import Order
from sqlalchemy.orm import Session


def criar_ordem_service(order_data: OrderSchema, db: Session) -> OrderResultSchema:
    data_venda = datetime.now(timezone.utc)

    nova_ordem = Order(
        cd_usuario=order_data.cd_usuario,
        vl_total=order_data.vl_total,
        qtd_total=order_data.qtd_total,
        dt_venda=data_venda
    )

    ordem_criada = criar_ordem(db, nova_ordem)

    return OrderResultSchema(
        cd_ordem=ordem_criada.cd_ordem,
        cd_usuario=ordem_criada.cd_usuario,
        vl_total=ordem_criada.vl_total,
        qtd_total=ordem_criada.qtd_total,
        dt_venda=ordem_criada.dt_venda
    )
