from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from database import get_db
from services.user_service import UserService
from models import Usuario
 
 
router = APIRouter()
 
 
@router.post("/login/")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = UserService.validate_user(db, username, password)
   
    if not user:
            raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
   
    return {"status": "success", "message": "Login realizado com sucesso"}

@router.post('/create_usuario/')
def create_usuario(userDescription: str = Form(...), password: str = Form(...), email: str = Form(...), username: str = Form(...), db: Session = Depends(get_db)):
  

    if not userDescription or not password or not email or not username:
        raise HTTPException(status_code=400, detail= "Nome, senha, email e código são obrigatórios!")
    
    novo_usuario = Usuario(dc_usuario=userDescription, cd_senha=password, dc_email=email, cd_usuario=username)
    result = UserService.create_user(db, novo_usuario)  

   
    if result == None:
        raise HTTPException(status_code=400, detail= f"Usuário {username} já existe!")
    
    return {"status": "success", "message": "Usuário cadastrado com sucesso!"}
    
