from fastapi import FastAPI
from database import engine
from models import Base
from fastapi.middleware.cors import CORSMiddleware
from config import URL_FRONT
import routes
import uvicorn
 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=URL_FRONT, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
 
app.include_router(routes.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)