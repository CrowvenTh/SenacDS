create schema notaFiscal;
use notaFiscal;

create table registro (
	id_nf int,
	id_item int,
	cod_prod int,
	valor_unit decimal(10,2),
	quantidade int,
	desconto int,
	primary key(id_nf, id_item, cod_prod)
);

INSERT INTO notaFiscal.registro (id_nf, id_item, cod_prod, valor_unit, quantidade, desconto) VALUES
(1, 1, 1, 25.00, 10, 5),
(1, 2, 2, 13.50, 3, NULL),
(1, 3, 3, 15.00, 2, NULL),
(1, 4, 4, 10.00, 1, NULL),
(1, 5, 5, 30.00, 1, NULL),
(2, 1, 3, 15.00, 4, NULL),
(2, 2, 4, 10.00, 5, NULL),
(2, 3, 5, 30.00, 7, NULL),
(3, 1, 1, 25.00, 5, NULL),
(3, 2, 4, 10.00, 4, NULL),
(3, 3, 5, 30.00, 5, NULL),
(3, 4, 2, 13.50, 7, NULL),
(4, 1, 5, 30.00, 10, 15),
(4, 2, 4, 10.00, 12, 5),
(4, 3, 1, 25.00, 13, 5),
(4, 4, 2, 13.50, 15, 5),
(5, 1, 3, 15.00, 3, NULL),
(5, 2, 5, 30.00, 6, NULL),
(6, 1, 1, 25.00, 22, 15),
(6, 2, 3, 15.00, 25, 20),
(7, 1, 1, 25.00, 10, 3),
(7, 2, 2, 13.50, 10, 4),
(7, 3, 3, 15.00, 10, 4),
(7, 4, 5, 30.00, 10, 1);


select * from registro;

-- A
select 
	id_nf, 
	id_item, 
	cod_prod, 
	valor_unit 
from registro 
	where desconto is null;

-- B
select 
	id_nf, 
	id_item, 
	cod_prod, 
	valor_unit,
	valor_unit - (valor_unit * (desconto / 100)) as 'valor vendido'
from registro 
	where desconto is not null;

-- C
update 
	registro 
		set desconto = 0 
where desconto is null;

select * from registro;

-- D
select
	id_nf, 
	id_item, 
	cod_prod, 
	valor_unit,
	(quantidade * valor_unit) as 'Valor total',
	(valor_unit - (valor_unit * (desconto / 100))) as 'valor vendido'
from registro;

-- E
select 
	id_nf,
	sum(quantidade * valor_unit) as 'Valor total'
	from registro 
		group by id_nf
			order by id_nf asc;

-- F
select
	id_nf,
	(sum(valor_unit - (valor_unit * (desconto / 100)))) as 'valor vendido'	
from registro
group by 1
order by 2 desc;

-- G
select
	cod_prod,
	sum(quantidade) as Quantidade
from registro
group by cod_prod;

-- H
select 
	id_nf,
	cod_prod,
		(sum(valor_unit - (valor_unit * (desconto / 100)))) as 'valor vendido'
		from registro
	group by 1, 2
having (sum(valor_unit - (valor_unit * (desconto / 100)))) > 10;

-- I
select
	id_nf,
	sum(quantidade * valor_unit) as 'valor total'
	from registro
group by 1
	having sum(quantidade * valor_unit) > 500;

-- J
select 
	cod_prod,
	round(avg(valor_unit - (valor_unit * (desconto / 100))),2) as 'Média Vendas'
from registro
	group by 1;

-- K
select 
	cod_prod,
	MIN(desconto) as 'Menor desconto',
	MAX(desconto) as 'Maior desconto',
	AVG(desconto) as 'Média desconto'
from registro
group by 1;

-- L
select 
	id_nf,
	count(quantidade) as 'Quantidade Itens'
from registro 
group by 1;
	
-- M
select 
	id_nf,
	id_item,
	cod_prod,
	valor_unit,
	quantidade,
		if(desconto > 0, 'Com desconto', 'Sem deconto') as 'status desconto',
	sum(valor_unit - (valor_unit * (desconto / 100))) as 'valor vendido'
from registro
group by 1, 2, 3;

-- N
select
	id_nf,
	id_item,
	cod_prod,
	quantidade,
		if(quantidade >= 10, 'Quantidade Alta', 'Quantidade Baixa') as 'Quantidade status'
from registro;

-- O
select
	id_nf,
	id_item,
	cod_prod,
	desconto,
		if(desconto > (select avg(desconto) from registro), 'Desconto Acima da Média',
			if(desconto = (select avg(desconto) from registro), 'Desconto Médio',
				if(desconto < (select avg(desconto) from registro) and desconto > 0, 'Desconto Abaixo da Média', 'Sem desconto'))) as 'desconto status'
	from registro;