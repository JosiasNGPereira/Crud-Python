import sqlite3

# Conexão com o banco de dados (ou criação se não existir)
conn = sqlite3.connect('estoque_vendas.db')

# Criação de um cursor
c = conn.cursor()

# Criação da tabela Cliente
c.execute('''CREATE TABLE IF NOT EXISTS Cliente (
             ID INTEGER PRIMARY KEY,
             nome VARCHAR(50) NOT NULL, 
             ID_endereco INTEGER NOT NULL,
             RG INTEGER NOT NULL,
             CPF INTEGER NOT NULL
             )''')

# Criação da tabela Telefone
c.execute('''CREATE TABLE IF NOT EXISTS Telefone (
             ID INTEGER PRIMARY KEY,
             ID_cliente INTEGER NOT NULL,
             numero VARCHAR(11) NOT NULL,
             FOREIGN KEY(ID_cliente) REFERENCES Cliente(ID)
             )''')

# Criação da tabela Endereco
c.execute('''CREATE TABLE IF NOT EXISTS Endereco (
             ID INTEGER PRIMARY KEY,
             ID_cliente INTEGER NOT NULL,
             cep VARCHAR(8) NOT NULL,
             cidade VARCHAR(30) NOT NULL,
             estado VARCHAR(2) NOT NULL,
             rua VARCHAR(30) NOT NULL,
             numero INTEGER NOT NULL,
             FOREIGN KEY(ID_cliente) REFERENCES Cliente(ID)
             )''')

# Criação da tabela Categoria
c.execute('''CREATE TABLE IF NOT EXISTS Categoria (
             ID INTEGER PRIMARY KEY,
             nome VARCHAR(50) NOT NULL
             )''')

# Criação da tabela Pedido
c.execute('''CREATE TABLE IF NOT EXISTS Pedido (
             ID INTEGER PRIMARY KEY,
             cod_cliente INTEGER NOT NULL,
             data_criacao DATE NOT NULL,
             data_prev_entrega DATE NOT NULL,
             valor_total FLOAT NOT NULL,
             status VARCHAR(30) NOT NULL,
             FOREIGN KEY(cod_cliente) REFERENCES Cliente(ID)
             )''')

# Criação da tabela Produto_Pedido
c.execute('''CREATE TABLE IF NOT EXISTS Produto_Pedido (
             cod_produto INTEGER NOT NULL,
             cod_pedido INTEGER NOT NULL,
             PRIMARY KEY (cod_produto, cod_pedido),
             FOREIGN KEY(cod_produto) REFERENCES Produto(ID),
             FOREIGN KEY(cod_pedido) REFERENCES Pedido(ID)
             )''')

# Criação da tabela Produto
c.execute('''CREATE TABLE IF NOT EXISTS Produto (
             id INTEGER PRIMARY KEY,
             name VARCHAR(50) NOT NULL,
             cod_Categoria INTEGER NOT NULL,
             tamanho VARCHAR(50),
             cor VARCHAR(50),
             preco_custos FLOAT NOT NULL,
             quantidade INTEGER NOT NULL,
             FOREIGN KEY(cod_Categoria) REFERENCES Categoria(ID)
             )''')

# Criação da tabela Venda
c.execute('''CREATE TABLE IF NOT EXISTS Venda (
             ID INTEGER PRIMARY KEY,
             cod_cliente INTEGER NOT NULL,
             cod_produto INTEGER NOT NULL,
             data_venda DATE NOT NULL,
             quantidade INTEGER NOT NULL,
             meio_venda VARCHAR(50) NOT NULL,
             FOREIGN KEY(cod_cliente) REFERENCES Cliente(ID),
             FOREIGN KEY(cod_produto) REFERENCES Produto(ID)
             )''')

# Criação da tabela OrdemProducao
c.execute('''CREATE TABLE IF NOT EXISTS OrdemProducao (
             ID INTEGER PRIMARY KEY,
             data_criacao DATE NOT NULL,
             semana INTEGER NOT NULL,
             status VARCHAR(30) NOT NULL
             )''')

# Criação da tabela OrdemProducao_Pedido
c.execute('''CREATE TABLE IF NOT EXISTS OrdemProducao_Pedido (
             cod_ordem INTEGER NOT NULL,
             cod_pedido INTEGER NOT NULL,
             PRIMARY KEY (cod_ordem, cod_pedido),
             FOREIGN KEY(cod_ordem) REFERENCES OrdemProducao(ID),
             FOREIGN KEY(cod_pedido) REFERENCES Pedido(ID)
             )''')

# Criação da tabela Estoque
c.execute('''CREATE TABLE IF NOT EXISTS Estoque (
             ID INTEGER PRIMARY KEY,
             cod_produto INTEGER NOT NULL,
             data_insercao DATE NOT NULL,
             quantidade INTEGER NOT NULL,
             operador VARCHAR(50) NOT NULL,
             FOREIGN KEY(cod_produto) REFERENCES Produto(ID)
             )''')

# Confirma as mudanças
conn.commit()

# Fecha a conexão
conn.close()
