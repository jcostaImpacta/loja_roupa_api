from sqlalchemy import Boolean, Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

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
    
    # categoria = relationship("Categoria", backref="produtos")
    # publico = relationship("Publico", backref="produtos")
    # genero = relationship("Genero", backref="produtos")
    # colecao = relationship("Colecao", backref="produtos")

# class Produtos(Base):
#     __tablename__ =  "T_PRODUTO"

#     id_produto = Column(Integer, primary_key=True, autoincrement=True)
#     dc_produto = Column(String(100), nullable=False)
#     tp_categoria = Column(Integer, ForeignKey("T_CATEGORIA.id_categoria"), nullable=False)
#     tp_publico = Column(Integer, ForeignKey("T_PUBLICO.id_publico"), nullable=False)
#     tp_genero = Column(Integer, ForeignKey("T_GENERO.id_genero"), nullable=False)
#     tp_colecao = Column(Integer, ForeignKey("T_COLECAO.id_colecao"), nullable=False)
#     vl_produto = Column(Numeric(10, 2), nullable=False, default=0)
#     qtd_produto = Column(Integer, nullable=False, default=0)
#     fl_ativo = Column(Boolean, default=True)
    
#     categoria = relationship("Categoria", backref="produtos")
#     publico = relationship("Publico", backref="produtos")
#     genero = relationship("Genero", backref="produtos")
#     colecao = relationship("Colecao", backref="produtos")

    # @property
    # def dc_categoria(self):
    #     return self.categoria.dc_categoria if self.categoria else None
    
    # @property
    # def dc_publico(self):
    #     return self.publico.dc_publico if self.publico else None
    
    # @property
    # def dc_genero(self):
    #     return self.genero.dc_genero if self.genero else None
    
    # @property
    # def dc_colecao(self):
    #     return self.colecao.dc_colecao if self.colecao else None

class Categoria(Base):
    __tablename__ =  "T_CATEGORIA"

    id_categoria = Column(Integer, primary_key=True)
    dc_categoria = Column(String(50), nullable=False)