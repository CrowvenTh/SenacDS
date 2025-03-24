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
	quantidade


