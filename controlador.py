#controlador
from modelo import inserir_produto, buscar_produto, deletar_produto, atualizar_produto

def processar_cadastro(nome, q_txt, p_txt):

    if nome == "" or p_txt == "" or q_txt == "":
        return False, "campos vazios!!"

    try:
        preco = float(p_txt)
        quantidade = int(q_txt)

    except ValueError:
        return False, "erro nos numeros!!"

    inserir_produto(nome, quantidade, preco)

    return True, "produto cadastrado!!"


def listar_produtos():
    return buscar_produto()


def remover_produto(id_produto):
    deletar_produto(id_produto)


def editar_produto(id_produto, nome, quantidade, preco):
    atualizar_produto(id_produto,nome,int(quantidade),float(preco))