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

insert into cliente(nome, pedido) values
("Thiago", "Notebook"),
("Thais", "Monitor"),
("Thalles", "Teclado");

insert into pedido(descricao, id_cliente) values
("Asus vivobook GO 15", 1),
("Dell monitor", 2),
("Teclado RGB horus", 3),
("Mousepad 70x30cm COD", 3);

alter table cliente add column pontos_fidelidade varchar(20) default 'regular';