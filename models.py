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
    