from modelo import inserir_produto
import tela

def processar_cadastro():
    nome = tela.cx_nome.get()
    q_txt = tela.cx_quantidade.get()
    p_txt = tela.cx_preco.get()

    if nome == "" or p_txt == "" or q_txt == "":
        tela.lbl_mensgem.configure(text="campos vazios!!",text_color="red")
        return

    try:
        preco = float(p_txt)
        quantidade = int(q_txt)
    except ValueError:
        tela.lbl_mensgem.configure(text="erro nos numeros!!",text_color="red")
        return

    inserir_produto(nome, quantidade, preco)
    tela.cx_nome.delete(0, "end")
    tela.cx_quantidade.delete(0, "end")
    tela.cx_preco.delete(0, "end")
    tela.lbl_mensgem.configure(text="produto cadastrado!!",text_color="green")