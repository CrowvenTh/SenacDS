drop schema universidade;
create schema universidade;
use universidade;

create table alunos(
	mat int,
	nome varchar(255),
	endereco varchar(255),
	cidade varchar(255),
		primary key (mat)
);

create table disciplinas(
	cod_disc varchar(10),
	nome_disc varchar(100), 
	carga_hor int,
		primary key (cod_disc)
);

create table professores(
	cod_prof int,
	nome varchar(255),
	endereco varchar(255),
	cidade varchar(255),
		primary key (cod_prof)
);

create table turma(
	cod_disc varchar(10), 
	cod_turma int, 
	cod_prof int, 
	ano year, 
	horario varchar(20),
		primary key (cod_disc, cod_turma, cod_prof, ano),
		foreign key(cod_disc) references disciplinas(cod_disc),
		foreign key(cod_prof) references professores(cod_prof)		
);

create table historico(
	mat int, 
	cod_disc varchar(10),
	cod_turma int,
	cod_prof int,
	ano year,
	frequencia int,
	nota decimal (10,2),
		primary key(mat, cod_disc, cod_turma, cod_prof, ano),
		foreign key(mat) references alunos(mat),
		foreign key(cod_disc) references disciplinas(cod_disc)		
);

insert into alunos(mat, nome, endereco, cidade) values
(2015010101, "JORGE DE ALENCAR", "RUA DAS ALMAS", "NATAL"),
(2015010102, "JOÃO PAULO", "AVENIDA RUY CARNEIRO", "JOÃO PESSOA"),
(2015010103, "MARINA", "RUA CARROSSEL", "RECIFE"),
(2015010104, "MARIA DAS DORES", "RUA DAS LADEIRAS", "FORTALEZA"),
(2015010105, "JOSUÉ EDUARDO DOS SANTOS", "CENTRO", "NATAL"),
(2015010106, "JOSUÉLISSON CLAUDINO DOS SANTOS", "CENTRO", "NATAL");

insert into disciplinas(cod_disc, nome_disc, carga_hor) values
("BD", "BANCO DE DADOS", 100),
("POO", "PROGRAMAÇÃO COM ACESSO A BANCO DE DADOS", 100),
("WEB", "AUTORIA WEB", 50),
("ENG", "ENGENHARIA DE SOFTWARE", 80);

insert into professores(cod_prof, nome, endereco, cidade) values
(212131, "NICKERSON FERREIRA", "RUA MANAÍRA", "JOÃO PESSOA"),
(122135, "ADORILSON BEZERRA", "AVENIDA SALGADO FILHO", "NATAL"),
(192011, "DIEGO OLIVEIRA", "AVENIDA ROBERTO FREIRE", "NATAL");

insert into turma(cod_disc, cod_turma, cod_prof, ano, horario) values
("BD", 1, 212131, 2015, "11H-12H"),
("BD", 2, 212131, 2015, "13H-14H"),
("POO", 1, 192011, 2015, "08H-09H"),
("WEB", 1, 192011, 2015, "07H-08H"),
("ENG", 1, 122135, 2015, "10H-11H");

insert into historico(mat, cod_disc, cod_turma, cod_prof, ano, frequencia, nota) values
(2015010101,'BD',1,212131,2015,5,9.00),
(2015010101,'ENG',1,122135,2015,1,10.00),
(2015010101,'POO',1,192011,2015,4,8.00),
(2015010101,'WEB',1,192011,2015,2,9.00),
(2015010102,'BD',1,212131,2015,3,7.00),
(2015010102,'ENG',1,122135,2015,7,6.90),
(2015010102,'POO',1,192011,2015,1,6.00),
(2015010102,'WEB',1,192011,2015,1,9.00),
(2015010103,'BD',1,212131,2015,10,4.00),
(2015010103,'ENG',1,122135,2015,4,7.50),
(2015010103,'POO',1,192011,2015,5,8.50),
(2015010103,'WEB',1,192011,2015,2,9.50),
(2015010104,'BD',1,212131,2015,2,7.00),
(2015010104,'ENG',1,122135,2015,6,8.50),
(2015010104,'POO',1,192011,2015,1,6.00),
(2015010104,'WEB',1,192011,2015,2,8.40),
(2015010105,'BD',1,212131,2015,4,5.50),
(2015010105,'ENG',1,122135,2015,8,6.00),
(2015010105,'POO',1,192011,2015,3,8.00),
(2015010105,'WEB',1,192011,2015,2,6.00),
(2015010106,'BD',1,212131,2015,2,4.90),
(2015010106,'ENG',1,122135,2015,1,10.00),
(2015010106,'POO',1,192011,2015,1,6.00),
(2015010106,'WEB',1,192011,2015,2,7.00);

-- A ----------
select 
	mat,
	nota
from historico
where cod_disc = 'BD' 
		and ano = 2015 
			and nota < 5;
-- B -------------
select 
	mat,
	avg(nota)
from historico
where cod_disc = 'POO' 
	and ano = 2015
group by mat;
-- C --------------
select
	mat,
	avg(nota) as média
from historico
where cod_disc = 'POO'
	and ano = 2015
group by 1
having avg(nota) > 6;
-- D --------------
select 
	* 
from alunos 
	where cidade != 'NATAL';

-- PARTE 02 ---------------------------------
-- INSERT -----------------------------------
-- A ----------------------------------------
select * from alunos;
insert into alunos (mat,nome,endereco,cidade) values
(2015010107, 'AUGUSTO ALEGRE','RUA MANGUEIRÃO','BELÉM'),
(2015010108, 'PEDRO ROCHA','AVENIDA NAZARÉ','BELÉM'),
(2015010109, 'ALEXA DIAS','TAGUATINGA','BRASÍLIA'),
(2015010110, 'RAISSA ANDREIA','SAMAMBAIA','BRASÍLIA');

-- B ----------------------------------------
insert into professores (cod_prof, nome, endereco, cidade) values
(777888,'ANTONIO SOARES','RIACHO FUNDO II','BRASÍLIA'),
(121721,'THIAGO ANTONIO','RIACHO FUNDO I','BRASÍLIA'),
(123968,'BRENA COSTA','NÚCLEO BANDEIRANTE','BRASÍLIA');

insert into turma(cod_disc, cod_turma, cod_prof, ano, horario) values 
('WEB',2,777888,2025,'9H-10H'),
('ENG',2,121721,2025,'12H-13H'),
('POO',2,123968,2025,'10H-11H');

-- C ----------------------------------------
insert into historico(mat, cod_disc, cod_turma, cod_prof, ano, frequencia, nota) values
(2015010107,'POO',2,123968,2025,8,8.8),
(2015010107,'WEB',2,777888,2025,9,7.8),
(2015010108,'ENG',2,121721,2025,5,5.4),
(2015010109,'WEB',2,777888,2025,10,8.0),
(2015010110,'ENG',2,121721,2025,7,9.2);

-- DELETE -----------------------------------
-- A ---------------------------------------
delete from historico where cod_turma = 2 and cod_disc = 'BD';

-- B ---------------------------------------
-- delete from alunos where mat > 2015010109; ERRO DE FK
-- update alunos set mat = 0 where mat > 2015010109; ERRO DE FK
update alunos set nome = null, endereco = null, cidade = null where mat > 2015010109;
select * from alunos where mat > 2015010109;


-- UDPATE -----------------------------------
-- A ----------------------------------------
update historico set nota = nota + 0.5 where cod_disc = 'ENG' and cod_turma = 2;

select nota from historico where cod_disc = 'ENG' and cod_turma = 2;
-- B ----------------------------------------
update historico set nota = 10 where mat = 2015010102 and cod_disc = "POO";

select 
	mat, 
	nota
from historico
	where mat = 2015010102 and cod_disc like "POO";

-- PARTE 03 ---------------------------------
-- A ----------------------------------------
select 
	nome 
from alunos 
	where mat in (
	select
		mat 
	from historico 
		where cod_disc = "BD");

-- 1 ----------------------------------------

-- SUBSELECT
select 
	mat,
	nome,
	endereco,
	cidade
from alunos 
	where mat in (
	select 
		mat
	from historico
		where nota = 10);
-- com JOIN
select 
	* 
from alunos a  
	inner join historico h
		on a.mat = h.mat
where h.nota = 10;

-- 2 ----------------------------------------
-- SUBSELECT
select 
	* 
from alunos 
	where mat in (
	select 
		mat
	from historico 
		where nota >7);

-- com JOIN
select
	*
from alunos a 
	inner join historico h
		on a.mat = h.mat 
	where nota > 7;

-- 3 ----------------------------------------
select
	p.nome,
	count(cod_turma) as turmas
from professores p
	inner join turma t
		on p.cod_prof = t.cod_prof
group by 1
having count(cod_turma) > 1;

-- 4 ----------------------------------------
select 
	a.nome,
	d.cod_disc,
	avg(h.nota), 
	round((select avg(h.nota) from historico h)) as "media geral"
from alunos a
	inner join historico h
		on a.mat = h.mat
	inner join disciplinas d
		on d.cod_disc = h.cod_disc
group by 1, 2;

-- --------------------------------------------------
-- INNER JOIN ---------------------------------------

-- 1
select
	a.nome, 
	d.nome_disc,
	h.nota
from alunos a
	inner join historico h
		on a.mat = h.mat
	inner join disciplinas d
		on d.cod_disc = h.cod_disc
where nota > 7 and ano = 2015;

-- 2
select
	p.nome,
	d.nome_disc,
	t.horario
from professores p
	inner join turma t
		on p.cod_prof = t.cod_prof
	inner join disciplinas d
		on d.cod_disc = t.cod_disc
where t.ano = 2015;

-- 3
select
	a.nome,
	d.nome_disc as disciplina,
	t.ano
	from alunos a
		inner join historico h
			on a.mat = h.mat
		inner join disciplinas d
			on d.cod_disc = h.cod_disc
		inner join turma t
			on d.cod_disc = t.cod_disc
		inner join professores p
			on t.cod_prof = p.cod_prof
where p.nome like "NICKERSON FERREIRA";

-- 4
select 
	a.nome,
	d.nome_disc,
	h.frequencia
from alunos a
	inner join historico h
		on a.mat = h.mat
	inner join disciplinas d
		on h.cod_disc = d.cod_disc
where a.cidade like "NATAL" and h.frequencia < 5;

-- 5
select 
	d.nome_disc,
	a.cidade,
	round(avg(h.nota), 2) as "média"
from alunos a
	inner join historico h
		on a.mat = h.mat
	inner join disciplinas d
		on d.cod_disc = h.cod_disc
group by 1, 2
order by nome_disc and avg(h.nota) desc;
	 
-- 6
select 
	p.nome,
	d.nome_disc as disciplina
from professores p
	join turma t
		on t.cod_prof = p.cod_prof
	join disciplinas d
		on d.cod_disc = t.cod_disc
where d.carga_hor > 70;

-- 7 -- CORRIGIR
select 
	a.nome,
round(avg(h.nota), 2) as nota
from alunos a
	inner join historico h
		on a.mat = h.mat
where h.cod_disc = "BD"
group by 1;

-- 8
select
	p.nome as professor,
	count(a.mat) as alunos
from alunos a
	inner join historico h
		on a.mat = h.mat
	inner join disciplinas d
		on d.cod_disc = h.cod_disc
	inner join turma t
		on t.cod_disc = d.cod_disc
	inner join professores p
		on p.cod_prof = t.cod_prof
where t.ano = 2015
group by 1
order by 2 desc;

-- 9 -- CORRIGIR
select
	a.nome as aluno,
	p.nome as professor,
	count(d.cod_disc) as disciplinas
from alunos a
	inner join historico h
		on a.mat = h.mat
	inner join disciplinas d
		on d.cod_disc = h.cod_disc
	inner join turma t
		on t.cod_disc = d.cod_disc
	inner join professores p
		on p.cod_prof = t.cod_prof
where t.ano = 2015 and a.nome is not null
group by 1, 2
having count(d.cod_disc) > 1;

-- 10
select
	d.nome_disc as disciplinas,
	a.cidade
from alunos a
	inner join historico h
		on a.mat = h.mat
	inner join disciplinas d
		on d.cod_disc = h.cod_disc
group by 1, 2;

-- Universidade 5 --------------------------------

-- Inserções adicionais para criar cenários mais complexos

-- Novas disciplinas
INSERT INTO Disciplinas VALUES
('REDES', 'REDES DE COMPUTADORES', 60),
('SO', 'SISTEMAS OPERACIONAIS', 80),
('IA', 'INTELIGÊNCIA ARTIFICIAL', 90);

-- Novos professores
INSERT INTO Professores VALUES
(312141, 'MARIA FERNANDA', 'AVENIDA ENGENHEIRO ROBERTO FREIRE', 'NATAL'),
(422142, 'CARLOS EDUARDO', 'RUA DO CATETE', 'RECIFE');

-- Novas turmas
INSERT INTO Turma VALUES
('BD', 3, 122135, 2016, '14H-15H'),
('POO', 2, 192011, 2016, '09H-10H'),
('REDES', 1, 312141, 2016, '16H-17H'),
('SO', 1, 422142, 2016, '13H-14H'),
('IA', 1, 422142, 2016, '15H-16H');

INSERT INTO Alunos VALUES
(2015010111, 'ALUNO SEM HISTÓRICO', 'RUA TESTE', 'NATAL'),
(2015010112, 'OUTRO ALUNO SEM NOTAS', 'AVENIDA TESTE', 'RECIFE');

INSERT INTO Disciplinas VALUES
('TESTE', 'DISCIPLINA SEM TURMA', 40),
('LAB', 'LABORATÓRIO SEM PROFESSOR', 60);

INSERT INTO Professores VALUES
(999991, 'PROFESSOR SEM TURMA', 'RUA SEM AULA', 'NATAL'),
(999992, 'OUTRO PROFESSOR INATIVO', 'AVENIDA SEM DISCIPLINA', 'JOÃO PESSOA');

INSERT INTO Turma VALUES
('BD', 9, 212131, 2016, '18H-19H'),  -- Turma sem alunos
('WEB', 5, 192011, 2016, '19H-20H'); -- Turma sem registros

-- Disciplinas que não possuem turmas cadastradas
INSERT INTO Disciplinas (COD_DISC, nome_disc, carga_hor) VALUES
('DSWEB', 'DESENVOLVIMENTO WEB', 80),
('MOBILE', 'PROGRAMAÇÃO MOBILE', 60),
('CLOUD', 'COMPUTAÇÃO EM NUVEM', 70);

-- Professores que não ministram nenhuma disciplina/turma
INSERT INTO Professores (COD_PROF, nome, endereco, cidade) VALUES
(505050, 'PROFESSOR SEM AULA', 'RUA DOS TESTES, 123', 'NATAL'),
(606060, 'DOCENTE SEM TURMA', 'AVENIDA DOS EXERCÍCIOS, 456', 'RECIFE'),
(707070, 'INSTRUTOR INATIVO', 'TRAVESSA DOS JOINs, 789', 'FORTALEZA');

-- Alunos totalmente isolados (sem relação com nenhuma outra tabela)
INSERT INTO Alunos (MAT, nome, endereco, cidade) VALUES
(99999991, 'ALUNO ISOLADO 1', 'RUA SEM RELAÇÃO, 1', 'NATAL'),
(99999992, 'ALUNO SEM VÍNCULOS', 'AV. SEM JOIN, 2', 'RECIFE'),
(99999993, 'ESTUDANTE SEM HISTÓRICO', 'TRAV. SEM DADOS, 3', 'FORTALEZA'),
(99999994, 'NOVATO SEM MATRÍCULA', 'BECO SEM NOTAS, 4', 'JOÃO PESSOA'),
(99999995, 'CALOURO SEM REGISTROS', 'ALAMEDA VAZIA, 5', 'NATAL');

-- lista 1 --
-- 1
select 
	a.nome as Aluno, 
	d.nome_disc as Disciplina,
	h.nota as Nota
from alunos a	
	inner join historico h
		on a.mat = h.mat
	inner join disciplinas d
		on h.cod_disc = d.cod_disc
where h.nota > 7 and h.ano = 2015; 

-- 2
select 
	p.nome as Professor,
	d.nome_disc as Disciplina,
	t.horario as Horário
from professores p
	inner join turma t
		on p.cod_prof = t.cod_prof
	inner join disciplinas d
		on d.cod_disc = t.cod_disc
where t.ano = 2015;

-- 3
select
	a.nome as Alunos
from alunos a
	inner join historico h
		on a.mat = h.mat
	inner join turma t
		on h.cod_turma = t.cod_turma
	inner join professores p
		on t.cod_prof = p.cod_prof
where p.nome = "NICKERSON FERREIRA";

-- 4
select
	round(avg(h.nota), 2) as Nota,
	d.nome_disc as Disciplina,
	a.cidade as Cidade
from alunos a
	inner join historico h
		on a.mat = h.mat
	inner join turma t
		on h.cod_turma = t.cod_turma
	inner join disciplinas d
		on t.cod_disc = d.cod_disc
group by 2, 3
order by 2, 1; 

-- 5
select
	p.nome as Professor,
	d.nome_disc as Disciplina,
	d.carga_hor as "Carga Horária"
from professores p
	inner join turma t
		on p.cod_prof = t.cod_prof
	inner join disciplinas d
		on d.cod_disc = t.cod_disc
where d.carga_hor > 70;

