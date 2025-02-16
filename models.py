from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "T_USUARIO"

    cd_usuario = Column(String(20), primary_key=True)
    dc_usuario = Column(String(30))
    cd_senha = Column(String(20))
    dc_email = Column(String(20))

# class Produto(Base):
#     __tablename__ = "T_USUARIO"

#     id_produto = Column(Integer, primary_key=True, autoincrement=True)
#     dc_produto = Column(String(50))
#     qtd_produto = Column(Integer, default=0)
#     vl_produto = Column(DECIMAL(10, 2), default=0)
#     tp_produto = Column(Integer, ForeignKey("T_TP_PRODUTO.CD_TP_PRODUTO"))
#     cd_modelo = Column(Integer, ForeignKey("T_MODELO.CD_MODELO"))