create schema biblioteca;

use biblioteca;

create table autor (
	autor_id int,
	nome varchar(255),
	pais_origem varchar(150),
		primary key (autor_id)
);

create table livro (
	livro_id int,
	titulo varchar(255),
	ano_publicacao int,
	genero varchar(200),
	autor_id int,
		primary key (livro_id),
		foreign key (autor_id) references autor(autor_id)
);