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
    pass

def buscar_produto():
    pass

def atualizar_produto(id,novo_p):
    pass

def deletar_produto(id):
    pass