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