#modelo
import sqlite3 as sq

def conectar():
    return sq.connect("banco.db")

def criar_tabela():
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS produtos(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           produto TEXT NOT NULL,
                           quantidade INTEGER,
                           preço REAL
    )
""")
        print("tabela criada com sucesso")
    except sq.Error as erro:
        print(f"ocorreu um erro no banco: {erro}")

def inserir_produto(nome,quantidade,preco):
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO produtos (produto, quantidade, preço) VALUES (?, ?, ?)", (nome, quantidade, preco))
            conexao.commit()
    except sq.Error as erro:
        print(f"ocorreu um erro ao inserir o produto: {erro}")

def buscar_produto():
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM produtos")
            produtos = cursor.fetchall()
            return produtos
    except sq.Error as erro:
        print(f"ocorreu um erro ao buscar os produtos: {erro}")
        return []
    
def atualizar_produto(id_produto, nome, quantidade, preco):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE produtos
            SET produto = ?, quantidade = ?, preço = ?
            WHERE id = ?
        """, (nome, quantidade, preco, id_produto))
        conexao.commit()

def deletar_produto(id_produto):
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
            conexao.commit()
    except sq.Error as erro:
        print(f"ocorreu um erro ao deletar o produto: {erro}")