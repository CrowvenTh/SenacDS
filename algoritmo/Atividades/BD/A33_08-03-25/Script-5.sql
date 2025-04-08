CREATE DATABASE Produto;
USE Produto;

CREATE TABLE Produtos (
Codigo VARCHAR(3) PRIMARY KEY,
Descricao VARCHAR(50) UNIQUE,
Estoque INT NOT NULL DEFAULT 0
);

INSERT INTO Produtos VALUES ('001', 'Computador', 15);
INSERT INTO Produtos VALUES ('002', 'Monitor', 25);
INSERT INTO Produtos VALUES ('003', 'Teclado', 45);

CREATE TABLE ItensVenda(
Venda INT,
Cod_Produto VARCHAR(3),
Quantidade INT
);

DELIMITER $
CREATE TRIGGER Tgr_ItensVenda_Insert AFTER INSERT
ON ItensVenda
FOR EACH ROW
BEGIN
UPDATE Produtos SET Estoque = Estoque - NEW.Quantidade
WHERE Codigo = NEW.Cod_Produto;
END$
DELIMITER;

show triggers;

select * from produtos;

INSERT INTO ItensVenda VALUES (1, '002',3);
INSERT INTO ItensVenda VALUES (1, '002',1);
INSERT INTO ItensVenda VALUES (1, '003',5);