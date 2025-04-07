create schema projetofinalDB;
use projetofinalDB;

drop table clientes;

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
	saldo decimal(10,2) default 0.00,
	data_abertura date,
	status enum('Ativa', 'Inativa', 'Bloqueada') default 'Ativa',
		primary key(conta_id),
		foreign key(cliente_id) references clientes(cliente_id),
		foreign key(agencia_id) references agencias(agencia_id)
);

INSERT INTO Contas (cliente_id, agencia_id, tipo_conta, saldo, data_abertura, status)
VALUES
(1, 1, 'Corrente', 5000.00, '2020-01-10', 'Ativa');

select * from contas;

create table transacoes(
	transacao_id int auto_increment,
	conta_origem_id int,
	conta_destino_id int,
	tipo_transacao enum('Depósito', 'Saque', 'Transferencia','Pagamento'),
	valor decimal(10,2),
	data_transacao datetime default CURRENT_TIMESTAMP(),
	descricao varchar(255),
		primary key(transacao_id),
		foreign key(conta_origem_id) references contas(conta_id),
		foreign key(conta_destino_id) references contas(conta_id)
);