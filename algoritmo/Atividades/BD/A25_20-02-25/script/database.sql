create schema turma;
use turma;

create table aluno(
	id_aluno int auto_increment primary key,
	nome varchar(150) not null
);

create table trabalho(
	id_trabalho int auto_increment primary key,
	descricao varchar(255) not null,
	id_aluno int not null,
		foreign key (id_aluno) references aluno(id_aluno)
);
