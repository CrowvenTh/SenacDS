create schema Exercicio;
use Exercicio;

create table cliente(
	id_cliente int auto_increment primary key,
	nome varchar(150),
	pedido varchar(200)
);

create table pedido(
	id_pedido int auto_increment primary key,
	descricao varchar(255),
	id_cliente int not null,
		foreign key (id_cliente) references cliente(id_cliente)
);

