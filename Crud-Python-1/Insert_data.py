import sqlite3
from datetime import date

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect('estoque_vendas.db')

# Função para inserir endereços e retornar seus IDs
def insert_addresses(c, cliente_ids):
    addresses = [
        ("12345678", "Cidade A", "SP", "Rua A", 123, cliente_ids[0]),
        ("23456789", "Cidade B", "RJ", "Rua B", 456, cliente_ids[1]),
        ("34567890", "Cidade C", "MG", "Rua C", 789, cliente_ids[2]),
        ("45678901", "Cidade D", "ES", "Rua D", 101, cliente_ids[3]),
        ("56789012", "Cidade E", "BA", "Rua E", 112, cliente_ids[4]),
        ("67890123", "Cidade F", "RS", "Rua F", 131, cliente_ids[5]),
        ("78901234", "Cidade G", "PR", "Rua G", 415, cliente_ids[6]),
        ("89012345", "Cidade H", "SC", "Rua H", 161, cliente_ids[7]),
        ("90123456", "Cidade I", "PE", "Rua I", 718, cliente_ids[8]),
        ("01234567", "Cidade J", "DF", "Rua J", 192, cliente_ids[9])
    ]
    c.executemany("INSERT INTO Endereco (cep, cidade, estado, rua, numero, ID_cliente) VALUES (?, ?, ?, ?, ?, ?)", addresses)

# Função para inserir telefones e retornar seus IDs
def insert_phones(c, cliente_ids):
    phones = [
        (cliente_ids[0], "11987654321"),
        (cliente_ids[1], "21987654321"),
        (cliente_ids[2], "31987654321"),
        (cliente_ids[3], "41987654321"),
        (cliente_ids[4], "51987654321"),
        (cliente_ids[5], "61987654321"),
        (cliente_ids[6], "71987654321"),
        (cliente_ids[7], "81987654321"),
        (cliente_ids[8], "91987654321"),
        (cliente_ids[9], "11987654322")
    ]
    c.executemany("INSERT INTO Telefone (ID_cliente, numero) VALUES (?, ?)", phones)

# Função para inserir clientes e retornar seus IDs
def insert_clients(c):
    clients = [
        ("Cliente A", 1, "123456789", "12345678901"),
        ("Cliente B", 2, "223456789", "22345678901"),
        ("Cliente C", 3, "323456789", "32345678901"),
        ("Cliente D", 4, "423456789", "42345678901"),
        ("Cliente E", 5, "523456789", "52345678901"),
        ("Cliente F", 6, "623456789", "62345678901"),
        ("Cliente G", 7, "723456789", "72345678901"),
        ("Cliente H", 8, "823456789", "82345678901"),
        ("Cliente I", 9, "923456789", "92345678901"),
        ("Cliente J", 10, "133456789", "13345678901")
    ]
    c.executemany("INSERT INTO Cliente (nome, ID_endereco, RG, CPF) VALUES (?, ?, ?, ?)", clients)
    c.execute("SELECT ID FROM Cliente")
    return [row[0] for row in c.fetchall()]

# Função para inserir produtos
def insert_products(c):
    products = [
        ("Produto 1", 1, "Pequeno", "Vermelho", 10.5, 100),
        ("Produto 2", 1, "Médio", "Azul", 15.0, 200),
        ("Produto 3", 2, "Grande", "Verde", 20.0, 150),
        ("Produto 4", 2, "Pequeno", "Amarelo", 12.5, 120),
        ("Produto 5", 3, "Médio", "Roxo", 18.0, 180),
        ("Produto 6", 3, "Grande", "Branco", 25.0, 140),
        ("Produto 7", 4, "Pequeno", "Preto", 9.0, 90),
        ("Produto 8", 4, "Médio", "Cinza", 16.0, 160),
        ("Produto 9", 5, "Grande", "Marrom", 22.5, 110),
        ("Produto 10", 5, "Pequeno", "Laranja", 13.5, 130)
    ]
    c.executemany("INSERT INTO Produto (name, cod_Categoria, tamanho, cor, preco_custos, quantidade) VALUES (?, ?, ?, ?, ?, ?)", products)

# Função principal para inserir dados
def insert_data():
    conn = connect_db()
    c = conn.cursor()

    # Inserir clientes e obter IDs
    cliente_ids = insert_clients(c)

    # Inserir endereços para cada cliente
    insert_addresses(c, cliente_ids)

    # Inserir telefones para cada cliente
    insert_phones(c, cliente_ids)

    # Inserir produtos
    insert_products(c)

    conn.commit()
    conn.close()

insert_data()
