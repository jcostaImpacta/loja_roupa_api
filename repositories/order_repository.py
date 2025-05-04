from sqlalchemy.orm import Session
from models import Order

class OrderRepository:

    def criar_ordem(db: Session, nova_ordem: Order) -> Order:
        db.add(nova_ordem) 
        db.commit() 
        db.refresh(nova_ordem)  
        return nova_ordem
