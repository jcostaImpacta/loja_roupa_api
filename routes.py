from fastapi import APIRouter, Depends, HTTPException, Form, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.user_service import UserService
from services.product_service import ProductService
from schemas.produto_schema import CategoriaSchema, FiltroProdutoSchema, ProdutoSchema, PublicoSchema, GeneroSchema, ColecaoSchema
from models import Usuario
from fastapi import Body


 
 
router = APIRouter()
 

@router.post("/login/")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = UserService.validate_user(db, username, password)
    
    if not user:
            raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
    
    return {"status": "success", "message": "Login realizado com sucesso"}

@router.post('/create_user/')
def create_user(userDescription: str = Form(...), password: str = Form(...), email: str = Form(...), username: str = Form(...), db: Session = Depends(get_db)):
  

    if not userDescription or not password or not email or not username:
        raise HTTPException(status_code=400, detail= "Nome, senha, email e código são obrigatórios!")
    
    new_user = Usuario(dc_usuario=userDescription, cd_senha=password, dc_email=email, cd_usuario=username)
    result = UserService.create_user(db, new_user)  

    if result == None:
        raise HTTPException(status_code=400, detail= f"Usuário {username} já existe!")
    
    return {"status": "success", "message": "Usuário cadastrado com sucesso!"}

@router.post("/get_products/", response_model=list[ProdutoSchema])
def get_products(
    filtros: FiltroProdutoSchema = Body(...),
    db: Session = Depends(get_db)
):
    products = ProductService.get_products(db, filtros)
    return products

@router.get("/list/categoria/", response_model=list[CategoriaSchema])
def get_categorias(
    db: Session = Depends(get_db)
):
    categorias = ProductService.get_categorias(db)
   
    return categorias


@router.get("/list/publico/", response_model=list[PublicoSchema])
def get_publicos(
    db: Session = Depends(get_db)
):
    categorias = ProductService.get_publicos(db)
   
    return categorias

@router.get("/product/min_max_price/")
def get_min_max_price(db: Session = Depends(get_db)):
    result = ProductService.get_min_max_price(db)

    if not result or result.get("preco_min") is None or result.get("preco_max") is None:
        raise HTTPException(status_code=404, detail="Nenhum preço encontrado")

    return result


@router.get("/product/min_max_price/")
def get_min_max_price(db: Session = Depends(get_db)):
    result = ProductService.get_min_max_price(db)

    if not result or result.get("preco_min") is None or result.get("preco_max") is None:
        raise HTTPException(status_code=404, detail="Nenhum preço encontrado")

    return result


@router.get("/list/genero/", response_model=list[GeneroSchema])
def get_generos(
    db: Session = Depends(get_db)
):
    generos = ProductService.get_generos(db)
   
    return generos

@router.get("/list/colecao/", response_model=list[ColecaoSchema])
def get_colecoes(
    db: Session = Depends(get_db)
):
    colecoes = ProductService.get_colecoes(db)
   
    return colecoes