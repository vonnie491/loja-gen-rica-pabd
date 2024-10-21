CREATE TABLE usuarios(
	nome varchar(20) PRIMARY KEY,
	senha varchar(12),
	saldo float
);

CREATE TABLE produtos(
	nome varchar(20) PRIMARY KEY,
	preco float
);

CREATE TABLE compras(
	cod_compra SERIAL PRIMARY KEY,
	comprador varchar(20) not null,
	produto varchar(20) not null,
	efetivada bool,
	constraint fk_comprador FOREIGN KEY (comprador) references usuarios (nome),
	constraint fk_produto FOREIGN KEY (produto) references produtos (nome)
);

INSERT INTO produtos (nome,preco) VALUES ('produto1',18.5);
INSERT INTO produtos (nome,preco) VALUES ('produto2',20);
INSERT INTO produtos (nome,preco) VALUES ('produto3',19);