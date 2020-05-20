--ALTER TABLE pessoas
--CHANGE COLUMN profissao prof varchar(30)

--ALTER TABLE pessoas
--RENAME TO gafanhotos

 --CREATE TABLE IF NOT EXISTS cursos (
 --idcurso int,
 --nome VARCHAR(30) NOT NULL UNIQUE,
 --descricao TEXT,
 --carga INT,
 --totaulas INT,
 --ano date
 --) 
 
 drop table cursos
 select * from cursos
  
 ALTER TABLE cursos 
 ADD idcurso int

 ALTER TABLE cursos
 ADD  PRIMARY KEY(idcurso)

