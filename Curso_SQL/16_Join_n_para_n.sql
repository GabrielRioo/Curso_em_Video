CREATE TABLE pessoas_assistem_cursos (
id INT NOT NULL IDENTITY,
data DATE,
idpessoas INT,
idcurso INT,
PRIMARY KEY(id),
FOREIGN KEY(idpessoas) REFERENCES pessoas(id),
FOREIGN KEY(idcurso) REFERENCES cursos(idcurso)
)

SELECT * FROM cursos
SELECT * FROM pessoas
SELECT * FROM pessoas_assistem_cursos

INSERT INTO pessoas_assistem_cursos VALUES
('2015-12-22', '3', '5'),
('2014-07-25', '4', '10'),
('2015-05-12', '6', '1'),
('2016-10-02', '2', '7'),
('2012-08-05', '5', '8')

SELECT p.nome, c.nome FROM pessoas as p
JOIN pessoas_assistem_cursos as a
ON p.id = a.idpessoas
JOIN cursos as c
ON c.idcurso = a.idcurso
ORDER BY p.nome
