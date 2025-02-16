from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario
from schemas.usuario_schema import UsuarioSchema

router = APIRouter()

#login
@router.get("/get_usuario", response_model=list[UsuarioSchema])
def get_produtos(db: Session = Depends(get_db)):
    return db.query(Usuario).all()