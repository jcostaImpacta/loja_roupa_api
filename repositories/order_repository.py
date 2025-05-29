from sqlalchemy.orm import Session
from models import Order, OrderProduct

class OrderRepository:

    def criar_ordem(db: Session, nova_ordem: Order) -> Order:
        db.add(nova_ordem) 
        db.commit() 
        db.refresh(nova_ordem)  
        return nova_ordem
    
    def criar_ordem_produto(db: Session, nova_ordem_produto: OrderProduct) -> OrderProduct:
        db.add(nova_ordem_produto) 
        db.commit() 
        db.refresh(nova_ordem_produto)  
        return nova_ordem_produto
