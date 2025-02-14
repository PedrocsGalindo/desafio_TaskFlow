CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE tarefa(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(300) NOT NULL,
    status ENUM('pendente', 'em andamento', 'concluido') NOT NULL,
    usuario INT NOT NULL, 	
    FOREIGN KEY (usuario) REFERENCES usuario(id) ON DELETE CASCADE
);