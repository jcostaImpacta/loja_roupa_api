from config import SessionLocal
from sqlalchemy import text

def testar_conexao():
    try:
        # Cria uma sessão com o banco
        db = SessionLocal()
        # Executa uma query simples (por exemplo, pegar a data/hora atual do SQL Server)
        resultado = db.execute(text("SELECT GETDATE();"))
        for row in resultado:
            print("Conexão bem-sucedida! Data/Hora do servidor:", row[0])
    except Exception as e:
        print("Erro ao conectar ao banco:", e)
    finally:
        db.close()

if __name__ == "__main__":
    testar_conexao()
