from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    cd_usuario: str
    dc_usuario: str
    cd_senha: str
    dc_email: str

class UsuarioInfoSchema(BaseModel):
    cd_usuario: str
    dc_usuario: str

    class Config:
        from_attributes = True