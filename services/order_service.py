from datetime import datetime
import pytz
from schemas.order_schema import OrderSchema
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from models import Order, OrderProduct, Produtos
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

        for produto in order_data.lista_produtos:
            nova_ordem_produto = OrderProduct(
                id_ordem = ordem_criada.id_ordem,
                id_produto = produto["id_produto"],
                qtd_produto = produto["qtd_total"],
                vl_produto_venda = produto["vl_produto"]
            )

            OrderRepository.criar_ordem_produto(db, nova_ordem_produto)
            produto_update = Produtos(
                id_produto = produto["id_produto"],
                qtd_produto = produto["qtd_produto"] - produto["qtd_total"],
            )

            ProductRepository.update_qtd_produto(db,produto_update)

        return ordem_criada
