# loja_roupa_api

Projeto Cadastro - Loja de Roupas
Este projeto tem como objetivo desenvolver um sistema de cadastro para uma loja de roupas, como parte das atividades acadêmicas da faculdade.

🛠️ Tecnologias Utilizadas
[Especificar as tecnologias aqui]

📌 Padrões e Processos
📂 Estrutura de Branches
O projeto segue o fluxo Git Flow, utilizando as seguintes branches principais:

Main: Contém a versão estável do projeto.
Dev: Contém tudo que foi desenvolvido na sprint.
Homolog: Utilizada para testes antes da entrega final.

🔄 Processo de Desenvolvimento
Criar uma nova branch baseada na main.
Implementar a funcionalidade ou correção necessária.
Fazer merge para a branch homolog para testes e validação.
Após aprovação, integrar na main.

🏷️ Nomeação de Branches
Funcionalidades novas: feature/numero_tarefa_descricao
Correções de bugs: fix/numero_tarefa_descricao

Exemplo:

    feature/2_criacao_endpoint
    fix/5_correcao_cadastro

📌 Padrão de Commits
O projeto utiliza a seguinte convenção para mensagens de commit:

[FEAT] #numero descrição → Para novas funcionalidades.
[FIX] #numero descrição → Para correções de bugs.
[HOTFIX] #numero descrição → Para correções urgentes.

git commit -m "[FEAT] #2 Criação do EndPoint"
git commit -m "[FIX] #5 Correção do fluxo de cadastro"
git commit -m "[HOTFIX] #10 Ajuste crítico no login"


🚀 Como Executar o Projeto

1 - Criar ambiente virtual (uma das duas opções)
    python -m venv venv
    py -m venv venv

2 - Instalar dependência
    pip install -r requirements.txt

3 - para subir a API
    main.py


Configurar Banco de dados

1 - Criar arquivo de config
    na raiz do projeto, precisa criar um arquivo config.py.
    Este arquivo nunca será carregado no commit, pois serve para colocar sua senha
    de conexão com banco de dados.

    dentro do arquivo basta colar:

    AMBIENTE = "DEV"
    DATABASE_URL = f"mssql+pyodbc://@localhost/LOJA_ROUPAS_{AMBIENTE}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"

    caso queira fazer o login por user e senha, pode alterar a variável DATABASE_URL


📌 Contribuição
Contribuições são bem-vindas! Certifique-se de seguir os padrões estabelecidos antes de abrir um Pull Request.
