

set ansi_nulls on;
go
set quoted_identifier on;
go

print('Inicializando Script roupas_mssql_1_00.sql');
print('');
go


-- Comando 1
if not exists(select 1 from sys.sysdatabases where name = 'LOJA_ROUPAS_DEV')
	begin
			create database LOJA_ROUPAS_DEV;

			print('Criado database LOJA_ROUPAS_DEV.');
	end

go

-- Comando 2
if not exists(select 1 from sys.sysdatabases where name = 'LOJA_ROUPAS_HOMOLOG')
	begin
			create database LOJA_ROUPAS_HOMOLOG;

			print('Criado database LOJA_ROUPAS_HOMOLOG.');
	end

go

-- Comando 3
if not exists(select 1 from sys.sysdatabases where name = 'LOJA_ROUPAS_PROD')
	begin
			create database LOJA_ROUPAS_PROD;

			print('Criado database LOJA_ROUPAS_PROD.');
	end

go


-- Comando 4

use LOJA_ROUPAS_DEV

if not exists(select 1 from sys.tables where name = 'T_LOG_SCRIPTS')
	begin

			create table T_LOG_SCRIPTS(
				DC_ARQUIVO varchar(50),
				CD_COMANDO varchar(2),
				DC_COMANDO varchar(200)
			);

			print('Criado tabela T_LOG_SCRIPTS na base de DEV.');

			insert into T_LOG_SCRIPTS(
				DC_ARQUIVO,
				CD_COMANDO,
				DC_COMANDO
			) values
			(
				'roupas_mssql_1_00.sql',
				'01',
				'Cria database LOJA_ROUPAS_DEV'
			),
			(
				'roupas_mssql_1_00.sql',
				'04',
				'Cria tabela T_LOG_SCRIPTS na base de DEV'
			)

	end

go

-- Comando 4

use LOJA_ROUPAS_HOMOLOG

if not exists(select 1 from sys.tables where name = 'T_LOG_SCRIPTS')
	begin

			create table T_LOG_SCRIPTS(
				DC_ARQUIVO varchar(50),
				CD_COMANDO varchar(2),
				DC_COMANDO varchar(200)
			);

			print('Criado tabela T_LOG_SCRIPTS na base de HOMOLOG.');

			insert into T_LOG_SCRIPTS(
				DC_ARQUIVO,
				CD_COMANDO,
				DC_COMANDO
			) values
			(
				'roupas_mssql_1_00.sql',
				'02',
				'Cria database LOJA_ROUPAS_HOMOLOG'
			),
			(
				'roupas_mssql_1_00.sql',
				'05',
				'Cria tabela T_LOG_SCRIPTS na base de HOMOLOG'
			)

	end

go


-- Comando 5

use LOJA_ROUPAS_PROD

if not exists(select 1 from sys.tables where name = 'T_LOG_SCRIPTS')
	begin

			create table T_LOG_SCRIPTS(
				DC_ARQUIVO varchar(50),
				CD_COMANDO varchar(2),
				DC_COMANDO varchar(200)
			);

			print('Criado tabela T_LOG_SCRIPTS na base de PROD.');

			insert into T_LOG_SCRIPTS(
				DC_ARQUIVO,
				CD_COMANDO,
				DC_COMANDO
			) values
			(
				'roupas_mssql_1_00.sql',
				'03',
				'Cria database LOJA_ROUPAS_PROD'
			),
			(
				'roupas_mssql_1_00.sql',
				'06',
				'Cria tabela T_LOG_SCRIPTS na base de PROD'
			)

	end

go


