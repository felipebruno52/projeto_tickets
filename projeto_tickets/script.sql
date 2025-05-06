CREATE DATABASE sistema_tickets;

USE sistema_tickets;

CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    situacao CHAR(1) NOT NULL CHECK (situacao IN ('A', 'I')),
    data_alteracao DATETIME NOT NULL
);

CREATE TABLE tickets_entregues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_funcionario INT NOT NULL,
    quantidade INT NOT NULL,
    situacao CHAR(1) NOT NULL CHECK (situacao IN ('A', 'I')),
    data_entrega DATETIME NOT NULL,
    FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
);
