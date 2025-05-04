from datetime import datetime
import pytz
from schemas.order_schema import OrderSchema
from repositories.order_repository import OrderRepository
from models import Order
from sqlalchemy.orm import Session


class OrderService:

    @staticmethod
    def new_ordem(order_data: OrderSchema, db: Session):
        fuso_brasilia = pytz.timezone("America/Sao_Paulo")
        dt_ordem = datetime.now(fuso_brasilia)

        nova_ordem = Order(
            cd_usuario=order_data.cd_usuario,
            vl_total_ordem=order_data.vl_total_ordem,
            qtd_total_produto=order_data.qtd_total_produto,
            dt_ordem=dt_ordem
        )

        ordem_criada = OrderRepository.criar_ordem(db, nova_ordem)

        return ordem_criada
