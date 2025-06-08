set ansi_nulls on;
go
set quoted_identifier on;
go

print('Inicializando Script roupas_mssql_1_01.sql');
print('');
go

-- Comando 0
if exists(select 1 from dbo.T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '00')
begin
	insert into dbo.T_LOG_SCRIPTS (DC_ARQUIVO, DC_COMANDO, CD_COMANDO)
	values ('roupas_mssql_1_01.sql', 'Script roupas_mssql_1_01.sql já executado', '00');
	print 'Script roupas_mssql_1_01.sql já executado. Verificar Log de execução.';
end
else
begin
	insert into dbo.T_LOG_SCRIPTS (DC_ARQUIVO, DC_COMANDO, CD_COMANDO)
	values ('roupas_mssql_1_01.sql', 'Execução do script 01 iniciado', 0);
end
go

-- Comando 1
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '01')
begin
	if not exists(select 1 from sys.tables where name = 'T_USUARIO')
	begin
		create table T_USUARIO (
			CD_USUARIO char(20) primary key,
			DC_USUARIO varchar(30) not null,
			CD_SENHA char(20) not null,
			DC_EMAIL varchar(100)
		);

		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '01', 'Cria tabela T_USUARIO');
	end
end
else
begin
	print 'Comando 1 já executado. Verificar Log de execução.';
end
go

-- Comando 2
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '02')
begin
	if not exists(select 1 from sys.tables where name = 'T_CATEGORIA')
	begin
		create table T_CATEGORIA (
			ID_CATEGORIA INT IDENTITY(1,1) PRIMARY KEY,
			DC_CATEGORIA VARCHAR(50) NOT NULL
		);

		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '02', 'Cria tabela T_CATEGORIA');
	end
end
else
begin
	print 'Comando 2 já executado. Verificar Log de execução.';
end
go

-- Comando 3
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '03')
begin
	if not exists(select 1 from sys.tables where name = 'T_PUBLICO')
	begin
		CREATE TABLE T_PUBLICO (
			ID_PUBLICO INT IDENTITY(1,1) PRIMARY KEY,
			DC_PUBLICO VARCHAR(50) NOT NULL
		);

		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '03', 'Cria tabela T_PUBLICO');
	end
end
else
begin
	print 'Comando 3 já executado. Verificar Log de execução.';
end
go

-- Comando 4
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '04')
begin
	if not exists(select 1 from sys.tables where name = 'T_GENERO')
	begin
		CREATE TABLE T_GENERO (
			ID_GENERO INT IDENTITY(1,1) PRIMARY KEY,
			DC_GENERO VARCHAR(50) NOT NULL
		);

		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '04', 'Cria tabela T_GENERO');
	end
end
else
begin
	print 'Comando 4 já executado. Verificar Log de execução.';
end
go

-- Comando 5
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '05')
begin
	if not exists(select 1 from sys.tables where name = 'T_COLECAO')
	begin
		CREATE TABLE T_COLECAO (
			ID_COLECAO INT IDENTITY(1,1) PRIMARY KEY,
			DC_COLECAO VARCHAR(50) NOT NULL
		);

		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '05', 'Cria tabela T_COLECAO');
	end
end
else
begin
	print 'Comando 5 já executado. Verificar Log de execução.';
end
go

-- Comando 6
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '06')
begin
	if not exists(select 1 from sys.tables where name = 'T_PRODUTO')
	begin
		CREATE TABLE T_PRODUTO (
			ID_PRODUTO INT IDENTITY(1,1) PRIMARY KEY,
			DC_PRODUTO VARCHAR(100) NOT NULL,
			TP_CATEGORIA INT NOT NULL,
			TP_PUBLICO INT NOT NULL,
			TP_GENERO INT NOT NULL,
			TP_COLECAO INT NOT NULL,
			VL_PRODUTO MONEY NOT NULL DEFAULT 0,
			QTD_PRODUTO INT NOT NULL DEFAULT 0,
			FL_ATIVO BIT DEFAULT 1
		);

		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '06', 'Cria tabela T_PRODUTO');
	end
end
else
begin
	print 'Comando 6 já executado. Verificar Log de execução.';
end
go


-- Comando 7
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '07')
begin
	if object_id('FK_PRODUTO_CATEGORIA', 'F') is null
	begin
		alter table T_PRODUTO add constraint FK_PRODUTO_CATEGORIA foreign key (TP_CATEGORIA) references T_CATEGORIA(ID_CATEGORIA);
		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '07', 'Chave estrangeira FK_PRODUTO_CATEGORIA criada na T_PRODUTO');
	end
end
else
begin
	print 'Comando 7 já executado. Verificar Log de execução.';
end
go

-- Comando 8
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '08')
begin
	if object_id('FK_PRODUTO_PUBLICO', 'F') is null
	begin
		alter table T_PRODUTO add constraint FK_PRODUTO_PUBLICO foreign key (TP_PUBLICO) references T_PUBLICO(ID_PUBLICO);
		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '08', 'Chave estrangeira FK_PRODUTO_PUBLICO criada na T_PRODUTO');
	end
end
else
begin
	print 'Comando 8 já executado. Verificar Log de execução.';
end
go

-- Comando 9
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '09')
begin
	if object_id('FK_PRODUTO_GENERO', 'F') is null
	begin
		alter table T_PRODUTO add constraint FK_PRODUTO_GENERO foreign key (TP_GENERO) references T_GENERO(ID_GENERO);
		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '09', 'Chave estrangeira FK_PRODUTO_GENERO criada na T_PRODUTO');
	end
end
else
begin
	print 'Comando 9 já executado. Verificar Log de execução.';
end
go

-- Comando 10
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '10')
begin
	if object_id('FK_PRODUTO_COLECAO', 'F') is null
	begin
		alter table T_PRODUTO add constraint FK_PRODUTO_COLECAO foreign key (TP_COLECAO) references T_COLECAO(ID_COLECAO);
		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '10', 'Chave estrangeira FK_PRODUTO_COLECAO criada na T_PRODUTO');
	end
end
else
begin
	print 'Comando 10 já executado. Verificar Log de execução.';
end
go

-- Comando 11
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '11')
begin
	if not exists(select 1 from sys.tables where name = 'T_ORDEM')
	begin
		create table T_ORDEM(
			ID_ORDEM INT IDENTITY(1,1) PRIMARY KEY,
			CD_USUARIO CHAR(20) NOT NULL,
			DT_ORDEM DATETIME NOT NULL DEFAULT GETDATE(),
			VL_TOTAL_ORDEM MONEY NOT NULL DEFAULT 0,
			QTD_TOTAL_PRODUTO INT NOT NULL
		);
		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '11', 'Criação da tabela T_ORDEM');
	end
end
else
begin
	print 'Comando 11 já executado. Verificar Log de execução.';
end
go

-- Comando 12
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '12')
begin
	if object_id('FK_ORDEM_USUARIO', 'F') is null
	begin
		alter table T_ORDEM add constraint FK_ORDEM_USUARIO foreign key (CD_USUARIO) references T_USUARIO(CD_USUARIO);
		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '12', 'Chave estrangeira FK_ORDEM_USUARIO criada na tabela T_ORDEM');
	end
end
else
begin
	print 'Comando 12 já executado. Verificar Log de execução.';
end
go

-- Comando 13
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '13')
begin
	if not exists(select 1 from sys.tables where name = 'T_ORDEM_PRODUTO')
	begin
		create table T_ORDEM_PRODUTO(
			ID_ORDEM INT NOT NULL,
			ID_PRODUTO INT NOT NULL,
			QTD_PRODUTO INT NOT NULL DEFAULT 0,
			VL_PRODUTO_VENDA MONEY NOT NULL DEFAULT 0
		);
		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '13', 'Criação da tabela T_ORDEM_PRODUTO');
	end
end
else
begin
	print 'Comando 13 já executado. Verificar Log de execução.';
end
go

-- Comando 14
if not exists(select 1 from T_LOG_SCRIPTS where DC_ARQUIVO = 'roupas_mssql_1_01.sql' and CD_COMANDO = '14')
begin
	if object_id('FK_ORDEM_PRODUTO_ORDEM', 'F') is null and object_id('FK_ORDEM_PRODUTO_PRODUTO', 'F') is null
	begin
		alter table T_ORDEM_PRODUTO add constraint FK_ORDEM_PRODUTO_ORDEM foreign key (ID_ORDEM) references T_ORDEM(ID_ORDEM);
		alter table T_ORDEM_PRODUTO add constraint FK_ORDEM_PRODUTO_PRODUTO foreign key (ID_PRODUTO) references T_PRODUTO(ID_PRODUTO);
		insert into T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
		values ('roupas_mssql_1_01.sql', '14', 'Criação das FKs FK_ORDEM_PRODUTO_ORDEM e FK_ORDEM_PRODUTO_PRODUTO na tabela T_ORDEM_PRODUTO');
	end
end
else
begin
	print 'Comando 14 já executado. Verificar Log de execução.';
end
go

-- Finalização
insert into dbo.T_LOG_SCRIPTS (DC_ARQUIVO, CD_COMANDO, DC_COMANDO)
values ('roupas_mssql_1_01.sql', '99', 'Script roupas_mssql_1_01.sql finalizado com sucesso');
print 'Script roupas_mssql_1_01.sql finalizado com sucesso';
go

print('');
print('Finalizando Script (1 - 01).');
go
