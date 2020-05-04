create database cadastro2
use cadastro2
CREATE TABLE pessoas (
id int NOT NULL IDENTITY,
nome varchar(30) NOT NULL,
idade DATE,
peso DECIMAL(5,2),
altura DECIMAL(3,2),
nacionalidade varchar(30) DEFAULT 'Brasil',
PRIMARY KEY (id)
) 

select * from pessoas