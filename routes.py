from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from database import get_db
from services.user_service import UserService
 
 
router = APIRouter()
 
 
@router.post("/login/")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = UserService.validate_user(db, username, password)
   
    if not user:
            raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
   
    return {"status": "success", "message": "Login realizado com sucesso"}