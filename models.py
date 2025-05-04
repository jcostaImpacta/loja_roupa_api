from sqlalchemy import Boolean, Column, Integer, Numeric, String, Float, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
from datetime import datetime
from datetime import datetime, timezone
from database import Base


Base = declarative_base()

class Usuario(Base):
    __tablename__ = "T_USUARIO"

    cd_usuario = Column(String(20), primary_key=True)
    dc_usuario = Column(String(30))
    cd_senha = Column(String(20))
    dc_email = Column(String(20))

class Produtos(Base):
    __tablename__ =  "T_PRODUTO"

    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    dc_produto = Column(String(100), nullable=False)
    tp_categoria = Column(Integer,  nullable=False)
    tp_publico = Column(Integer, nullable=False)
    tp_genero = Column(Integer,  nullable=False)
    tp_colecao = Column(Integer,  nullable=False)
    vl_produto = Column(Numeric(10, 2), nullable=False, default=0)
    qtd_produto = Column(Integer, nullable=False, default=0)
    fl_ativo = Column(Boolean, default=True)

class Categoria(Base):
    __tablename__ =  "T_CATEGORIA"

    id_categoria = Column(Integer, primary_key=True)
    dc_categoria = Column(String(50), nullable=False)

class Publico(Base):
    __tablename__ =  "T_PUBLICO"

    id_publico = Column(Integer, primary_key=True)
    dc_publico = Column(String(50), nullable=False)

class Genero(Base):
    __tablename__ =  "T_GENERO"

    id_genero = Column(Integer, primary_key=True)
    dc_genero = Column(String(50), nullable=False)

class Colecao(Base):
    __tablename__ =  "T_COLECAO"

    id_colecao = Column(Integer, primary_key=True)
    dc_colecao = Column(String(50), nullable=False)

class Order(Base):
    __tablename__ = 'T_ORDEM'

    id_ordem = Column(Integer, primary_key=True, autoincrement=True)
    cd_usuario = Column(String(20), nullable=False)
    vl_total_ordem = Column(Float, nullable=False)
    qtd_total_produto = Column(Integer, nullable=False)
    dt_ordem = Column(DateTime, nullable=False)