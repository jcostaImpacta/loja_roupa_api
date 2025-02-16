from fastapi import FastAPI
from database import engine
from models import Base
import routes
import uvicorn

app = FastAPI()

# Criar as tabelas automaticamente
Base.metadata.create_all(bind=engine)

# Incluir rotas
app.include_router(routes.router)

@app.get("/")
def home():
    return {"mensagem": "API da Loja de Roupas está rodando!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)