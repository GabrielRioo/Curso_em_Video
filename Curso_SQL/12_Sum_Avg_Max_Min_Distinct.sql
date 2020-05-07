select * from cursos
where nome like 'P%'

select * from cursos
where nome not like '%A%'

select * from cursos
where nome like 'PH%p_'

select distinct nacionalidade from pessoas

SELECT COUNT(*) FROM pessoas

SELECT MAX(carga) FROM cursos

SELECT MIN(carga) FROM cursos

SELECT SUM(totaulas) FROM cursos

SELECT AVG(totaulas) FROM cursos

SELECT * FROM pessoas

-- EXERCICIOS
--#1
select nome from gafanhotos where sexo = 'F' order by nome;
--#2
select * from gafanhotos where nascimento between '2000-01-01' and '2015-12-31' order by nome;
--#3
select nome,profissao from gafanhotos where profissao = 'programador' and sexo = 'M' order by nome;
--#4
select * from gafanhotos where sexo = 'F' and nome like 'j%' and nacionalidade = 'brasil' order by nome;
--#5
select nome,nacionalidade from gafanhotos where sexo = 'M' and nome like '%silva%' 
and peso < '100' and nacionalidade != 'brasil' order by nome;
--#6
select max(altura) from gafanhotos where sexo = 'M' and nacionalidade = 'brasil' order by nome;
--#7
select avg(peso) from gafanhotos;
--#8
select min(peso) from gafanhotos where sexo = 'F' and 
nascimento between '1990-01-01' and '2000-12-31' and nacionalidade != 'brasil' ;
--#9
select count(nome) from gafanhotos where sexo = 'F' and altura > '1.90';