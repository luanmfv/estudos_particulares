#gerenciador de banco de dados, suporta alto volumes, funcional em site com acessos simultaneos

- Open source, utilização gratuita

- Extensões, trabalhar com outros tipos de dados e linguagem, como python

- SGBD (Sistema de gerenciamento de banco de dados), postgresql é um dos 4 maior, dentre eles existem oracle, mysql e sql server

comandos

CREATE DATABASE nomedoarquivo;  #criar
DROP DATABASE nomedoarquivo;    #deletar



-----------------------------------------------------------------------------------------------

SERIAL, NOT NULL, UNIQUE, INT, CREATE TABLE, ID SERIAL PRIMARY KEY, VARCHAR

/*

Para criar uma coluna, e o nome é usuarios

SERIAL significa que ele cadastra direto o por numero, usuario 1, 2 e etc

NOT NULL é para garantir que o campo não pode ser nulo

UNIQUE é para garantir que exista apenas um dele na tabela

idade INT para informar que será recebido um número inteiro

/* E */ para abrir e fechar anotações particulares que não interferiram na run do code

*/

CREATE TABLE usuarios (   
	id SERIAL PRIMARY KEY, 
	nome VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	idade INT,
	data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	

);

-----------------------------------------------------------------------------------------------

/*

INSERT INTO é para inserir dados na tabela
VALUES seriam os valores que você quer inserir
(não é obrigatório colocar as colunas nas quais você quer inserir, digitar (nome, email, idade, parece que o proprio sistema ja vai colocando de 1 em 1))

*/



INSERT INTO usuarios (nome, email, idade)
VALUES ('João', 'joao@gmail.com', 26);


-----------------------------------------------------------------------------------------------

SELECT * FROM usuarios;  (usuarios foi a tabela escolhida e * para ver tudo, mostra o que foi feito)


-----------------------------------------------------------------------------------------------


/*

ponto e virgula no final sempre

*/



INSERT INTO usuarios (nome, email, idade)
VALUES

('João', 'joao@gmail.com', 26),
('Ana', 'ana@gmail.com', 23),
('Luan', 'luan@gmail.com', 25),
('Renata', 'renata@gmail.com', 28),
('Alberta', 'alberta@gmail.com', 23);




