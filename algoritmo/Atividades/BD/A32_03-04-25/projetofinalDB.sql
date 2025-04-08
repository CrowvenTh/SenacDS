drop schema projetofinalDB;
create schema projetofinalDB;
use projetofinalDB;

create table clientes(
	cliente_id int auto_increment,
	nome varchar(150),
	cpf varchar(15),
	data_nascimento date,
	telefone varchar(15),
	email varchar(50),
	endereco varchar(255),
	data_cadastro datetime default CURRENT_TIMESTAMP(),
		primary key (cliente_id)
);

select * from clientes;

INSERT INTO Clientes (nome, cpf, data_nascimento, telefone, email, endereco) 
VALUES 
('João Silva', '123.456.789-01', '1980-05-15', '(11) 98765-4321', 
'joao@email.com', 'Rua A, 100 - Centro');

create table agencias(
	agencia_id int auto_increment,
	nome varchar(150),
	endereco varchar(255),
	telefone varchar(15),
		primary key (agencia_id)
);

INSERT INTO Agencias (nome, endereco, telefone) VALUES
('Agência Centro', 'Rua Principal, 123 - Centro', '(11) 1234-5678');

select * from agencias;

create table contas(
	conta_id int auto_increment,
	cliente_id int,
	agencia_id int,
	tipo_conta enum('Corrente', 'Poupança', 'Salário'),
	saldo decimal(15,2) default 0.00,
	data_abertura date,
	status enum('Ativa', 'Inativa', 'Bloqueada') default 'Ativa',
		primary key(conta_id),
		foreign key(cliente_id) references clientes(cliente_id),
		foreign key(agencia_id) references agencias(agencia_id)
);

INSERT INTO Contas (cliente_id, agencia_id, tipo_conta, saldo, data_abertura, status)
values
(1, 1, 'Corrente', 5000.00, '2020-01-10', 'Ativa');


select * from contas;

create table transacoes(
	transacao_id int auto_increment,
	conta_origem_id int,
	conta_destino_id int,
	tipo_transacao enum('Depósito', 'Saque', 'Transferencia','Pagamento'),
	valor decimal(15,2),
	data_transacao datetime default CURRENT_TIMESTAMP(),
	descricao varchar(255),
		primary key(transacao_id),
		foreign key(conta_origem_id) references contas(conta_id),
		foreign key(conta_destino_id) references contas(conta_id)
);

INSERT INTO Transacoes (conta_origem_id, conta_destino_id, tipo_transacao, valor,
descricao) VALUES
(1, NULL, 'Depósito', 1000.00, 'Depósito inicial'),
(NULL, 2, 'Depósito', 2000.00, 'Depósito inicial');

create table emprestimos(
	emprestimo_id int auto_increment,
	conta_id int,
	valor decimal(15,2),
	taxa_juros decimal(5,2),
	parcelas int,
	valor_parcela decimal(15,2),
	data_contratacao date,
	status enum('Ativo','Quitado','Inadiplente') default 'Ativo',
		primary key(emprestimo_id),
		foreign key(conta_id) references contas(conta_id)
);

INSERT INTO Emprestimos (conta_id, valor, taxa_juros, parcelas, valor_parcela,
data_contratacao) VALUES
(1, 10000.00, 1.5, 12, 916.67, '2022-01-15');

create table pagamentosEmprestimos(
	pagamento_id int auto_increment,
	emprestimo_id int,
	numero_parcela int,
	valor_pago decimal(15,2),
	data_pagamento date,
		primary key(pagamento_id),
		foreign key(emprestimo_id) references emprestimos(emprestimo_id)
);

INSERT INTO PagamentosEmprestimos (emprestimo_id, numero_parcela, valor_pago,
data_pagamento) VALUES
(1, 1, 916.67, '2022-02-15');

-- PARTE III --

-- Inserir Agências
INSERT INTO Agencias (nome, endereco, telefone) VALUES
('Agência Centro', 'Rua Principal, 123 - Centro', '(11) 1234-5678'),
('Agência Norte', 'Avenida Secundária, 456 - Zona Norte', '(11) 2345-6789'),
('Agência Sul', 'Praça Terciária, 789 - Zona Sul', '(11) 3456-7890');

-- Inserir Clientes
INSERT INTO Clientes (nome, cpf, data_nascimento, telefone, email, endereco) VALUES
('João Silva', '123.456.789-01', '1980-05-15', '(11) 98765-4321', 'joao@email.com', 'Rua A, 100 - Centro'),
('Maria Oliveira', '234.567.890-12', '1985-08-20', '(11) 87654-3210', 'maria@email.com', 'Av. B, 200 - Norte'),
('Carlos Souza', '345.678.901-23', '1990-11-25', '(11) 76543-2109', 'carlos@email.com', 'Praça C, 300 - Sul'),
('Ana Pereira', '456.789.012-34', '1975-03-10', '(11) 65432-1098', 'ana@email.com', 'Rua D, 400 - Centro'),
('Pedro Costa', '567.890.123-45', '1995-07-30', '(11) 54321-0987', 'pedro@email.com', 'Av. E, 500 - Norte');

-- Inserir Contas
INSERT INTO Contas (cliente_id, agencia_id, tipo_conta, saldo, data_abertura, status) VALUES
(1, 1, 'Corrente', 5000.00, '2020-01-10', 'Ativa'),
(2, 2, 'Poupança', 8000.00, '2019-05-15', 'Ativa'),
(3, 3, 'Salário', 3000.00, '2021-03-20', 'Ativa'),
(4, 1, 'Corrente', 10000.00, '2018-11-05', 'Ativa'),
(5, 2, 'Poupança', 15000.00, '2020-07-30', 'Ativa'),
(1, 3, 'Poupança', 2000.00, '2021-02-18', 'Ativa');

-- Inserir Transações
INSERT INTO Transacoes (conta_origem_id, conta_destino_id, tipo_transacao, valor, descricao) VALUES
(1, NULL, 'Depósito', 1000.00, 'Depósito inicial'),
(NULL, 2, 'Depósito', 2000.00, 'Depósito inicial'),
(1, 2, 'Transferência', 500.00, 'Transferência para Maria'),
(3, NULL, 'Saque', 300.00, 'Saque em caixa eletrônico'),
(4, 5, 'Transferência', 1000.00, 'Pagamento de serviço');

-- Inserir Empréstimos
INSERT INTO Emprestimos (conta_id, valor, taxa_juros, parcelas, valor_parcela, data_contratacao) VALUES
(1, 10000.00, 1.5, 12, 916.67, '2022-01-15'),
(3, 5000.00, 2.0, 6, 883.33, '2022-02-20');

-- Inserir Pagamentos de Empréstimos
INSERT INTO PagamentosEmprestimos (emprestimo_id, numero_parcela, valor_pago, data_pagamento) VALUES
(1, 1, 916.67, '2022-02-15'),
(1, 2, 916.67, '2022-03-15'),
(2, 1, 883.33, '2022-03-20');

-- CONSULTAS --

-- A
select 
	cl.nome,
	sum(co.saldo) as 'Saldo Total'
from clientes cl
	inner join contas co
		on cl.cliente_id = co.cliente_id
group by 1;

-- B
select
	tipo_conta as 'Tipo de conta',
	round(avg(saldo), 2) as 'Saldo médio'
from contas
group by 1;

-- C
select
	tr.tipo_transacao,
	tr.valor,
	tr.data_transacao,
	tr.descricao
from clientes cl
	inner join contas co
		on cl.cliente_id = co.cliente_id
	inner join transacoes tr 
		on tr.conta_origem_id and tr.conta_origem_id = co.conta_id
where cl.cliente_id = 1;

-- D
select
	tipo_transacao,
	sum(valor) as total
from transacoes
where month(data_transacao) = month(curdate())
group by 1;

-- E
select
	cl.nome as Cliente,
	count(co.tipo_conta) as qtd	
from clientes cl
	inner join contas co
		on cl.cliente_id = co.cliente_id
		group by 1
having count(co.tipo_conta) > 1;

-- F
select 
	ag.nome as Agencia,
	count(em.emprestimo_id) as emprestimos
from emprestimos em
	inner join contas co
		on em.conta_id = co.conta_id
	inner join agencias ag
		on ag.agencia_id = co.agencia_id
group by 1;
