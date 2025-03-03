from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URL
from repositories.user_repository import UserRepository
from models import Usuario

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



# class Usuario(db.Model):
#     __tablename__ = 'T_USUARIO' 
#     cd_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True) 
#     dc_usuario = db.Column(db.String(100), nullable=False)  
#     cd_senha = db.Column(db.String(255), nullable=False)  
#     dc_email = db.Column(db.String(100), unique=True, nullable=False)  

#     def to_dict(self):
#         return {
#             "cd_usuario": self.cd_usuario,
#             "dc_usuario": self.dc_usuario,
#             "cd_senha": self.cd_senha,
#             "dc_email": self.dc_email
#         }



with app.app_context():
    db.create_all()

# Endpoint para cadastrar um novo usuário (POST)
@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json() 
    dc_usuario = data.get('dc_usuario')
    cd_senha = data.get('cd_senha')
    dc_email = data.get('dc_email')
    cd_codigo = data.get('cd_codigo')

    if not dc_usuario or not cd_senha or not dc_email:
        return jsonify({"error": "Nome, senha e email são obrigatórios!"}), 400

    # Verificar se usuário já existe
    usuario_existente = Usuario.query.filter_by(dc_email=dc_email).first()
    if usuario_existente:
        return jsonify({"error": "Usuário com esse email já existe!"}), 400

    # Criar novo usuário
    novo_usuario = Usuario(dc_usuario=dc_usuario, cd_senha=cd_senha, dc_email=dc_email, cd_codigo=cd_codigo)
    UserRepository.create_user(db, novo_usuario)
    

    return jsonify(novo_usuario.to_dict()), 201

# Listar todos os usuários (GET)
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200

if __name__ == '__main__':
    app.run(debug=True)
