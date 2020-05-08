sp_help pessoas

select * from pessoas

ALTER TABLE pessoas 
ADD COLUMN cursopreferido INT -- Em MySQL

ALTER TABLE pessoas  -- Em SQL Server
ADD cursopreferido INT

ALTER TABLE pessoas
ADD FOREIGN KEY (cursopreferido)
REFERENCES cursos(idcurso)

sp_help cursos
 
select * from cursos

ALTER TABLE cursos 
ALTER COLUMN idcurso INT NOT NULL  

ALTER TABLE cursos
ADD PRIMARY KEY (idcurso)

UPDATE pessoas set cursopreferido = '5'
WHERE id = 1

DELETE FROM cursos 
WHERE idcurso = '6'

select nome, cursopreferido from pessoas
--unir essas duas
select nome, ano from cursos

SELECT p.nome, p.cursopreferido, c.nome, c.ano 
FROM pessoas as p INNER JOIN cursos as c --INNER JOIN
ON c.idcurso = p.cursopreferido


SELECT p.nome, p.cursopreferido, c.nome, c.ano 
FROM pessoas as p LEFT OUTER JOIN cursos as c --INNER JOIN
ON c.idcurso = p.cursopreferido


SELECT p.nome, p.cursopreferido, c.nome, c.ano 
FROM pessoas as p RIGHT OUTER JOIN cursos as c --INNER JOIN
ON c.idcurso = p.cursopreferido