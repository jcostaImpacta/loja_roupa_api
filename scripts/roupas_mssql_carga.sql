
use LOJA_ROUPAS_DEV


INSERT INTO T_CATEGORIA (DC_CATEGORIA)
VALUES
	('Camiseta'),
	('Camisa'),
	('Calça'),
	('Shorts'),
	('Tênis'),
	('Sapato'),
	('Sandália'),
	('Vestido'),
	('Body'),
	('Biquini'),
	('Sunga'),
	('Óculos');

INSERT INTO T_PUBLICO (DC_PUBLICO) VALUES ('Adulto'), ('Infantil');

INSERT INTO T_GENERO (DC_GENERO) VALUES ('Masculino'), ('Feminino'), ('Unissex');

INSERT INTO T_COLECAO (DC_COLECAO) VALUES ('Verão'), ('Inverno'), ('Todas as Estações');


INSERT INTO T_PRODUTO (DC_PRODUTO, TP_CATEGORIA, TP_PUBLICO, TP_GENERO, TP_COLECAO, VL_PRODUTO, QTD_PRODUTO, FL_ATIVO) VALUES
('Camiseta Básica Branca', 1, 1, 3, 3, 39.90, 50, 1),
('Camisa Social Azul', 2, 1, 1, 3, 89.90, 30, 1),
('Calça Jeans Skinny', 3, 1, 2, 3, 129.90, 25, 1),
('Shorts Praia Floral', 4, 2, 3, 1, 59.90, 40, 1),
('Tênis Esportivo Preto', 5, 1, 1, 3, 199.90, 20, 1),
('Sapato Social Marrom', 6, 1, 1, 3, 249.90, 15, 1),
('Sandália Rasteira', 7, 1, 2, 1, 79.90, 35, 1),
('Vestido Floral Curto', 8, 2, 2, 1, 149.90, 18, 1),
('Body Bebê Algodão', 9, 2, 3, 3, 49.90, 50, 1),
('Biquini Listrado', 10, 1, 2, 1, 99.90, 22, 1),
('Sunga Estampada', 11, 1, 1, 1, 69.90, 30, 1),
('Óculos de Sol Aviador', 12, 1, 3, 3, 149.90, 10, 1),
('Camiseta Infantil Estampada', 1, 2, 3, 3, 34.90, 40, 1),
('Camisa Polo Verde', 2, 1, 1, 3, 79.90, 28, 1),
('Calça Moletom Cinza', 3, 1, 3, 2, 119.90, 20, 1),
('Shorts Jeans Destroyed', 4, 1, 2, 3, 89.90, 15, 1),
('Tênis Casual Branco', 5, 1, 3, 3, 179.90, 25, 1),
('Sapato Feminino Salto', 6, 1, 2, 3, 259.90, 10, 1),
('Vestido Longo Elegante', 8, 1, 2, 2, 199.90, 12, 1),
('Óculos de Grau Moderno', 12, 1, 3, 3, 189.90, 8, 1);


update T_PRODUTO set QTD_PRODUTO = 5 where ID_PRODUTO = 20
