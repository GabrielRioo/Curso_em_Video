select * from cursos

INSERT INTO cursos VALUES 
('1','HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2','Algoritimos', 'Logica de Programação', '20', '15', '2014'),
('3','Photoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4','PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('5','Jarva', 'Introdução à Linguagem Java', '10', '29', '2000'),
('6','MySQL', 'Banco de Daos MySQL', '30', '15', '2016'),
('7','Word', 'Curso Completo de Word', '40', '30', '2018'),
('8','Sapateado', 'Dança Ritmica', '40', '30', '2018'),
('9','Cozinha Árabe', 'Aprenda a fazer kibe', '40', '30', '2018'),
('10','Youtuber', 'Gerar Polêmica e ganhar inscritos', '5', '2', '2018')

INSERT INTO cursos VALUES
('7','Word', 'Curso Completo de Word', '40', '30', '2018')

UPDATE cursos
SET nome = 'HTML5'
WHERE idcurso = '1'

UPDATE cursos 
SET nome = 'PHP', ano = '2015'
WHERE idcurso = '4'

UPDATE cursos 
SET nome = 'Java', carga = '40', ano = '2015'
WHERE idcurso = '5'
-- LIMIT 1     MySQL

DELETE FROM cursos
WHERE idcurso = '8'

DELETE FROM cursos 
WHERE year(ano) = '2018'

TRUNCATE table cursos
