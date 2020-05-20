
select * from pessoas

INSERT INTO pessoas (nome, idade,peso, altura, nacionalidade) 
VALUES ('Cremilda', '1966-12-25', '93.5', '1.53', 'Portugal')

INSERT INTO pessoas (nome, idade,peso, altura) 
VALUES ('Josivaldo', '1946-12-25', '72.5', '1.73')

-- INSERT INTO pessoas (nome, idade,peso, altura, nacionalidade) - EM MYSQL
-- VALUES ('Josivaldo', '1946-12-25', '72.5', '1.73', DEFAULT)

INSERT INTO pessoas 
VALUES ('Adalgiza', '1986-10-08', '63.5', '1.68', 'Irlanda')

INSERT INTO pessoas (nome, idade, peso, altura, nacionalidade) VALUES
('Gabriel', '1997-08-15', '55.9', '1.72', 'Brasil'),
('Camila', '1998-08-19', '68.9', '1.62', 'Brasil'),
('Leonardo', '1998-05-12', '65.9', '1.82', 'Brasil')