import customtkinter as ctk
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from controlador import processar_cadastro
from modelo import buscar_produto, deletar_produto

def gerar_graficos():
    graficos = ctk.CTkButton(janela,text="GRAFICO")
    graficos.pack(pady=10)

def atualizar_graficos():
    area_produtos.delete("0.0","end")
    produtos = buscar_produto()
    for produto in produtos:
        texto = f"ID: {produto[0]} - Produto: {produto[1]} - Quantidade: {produto[2]} - Preço: {produto[3]}\n"
        area_produtos.insert("end", texto)
    if len(produtos) == 0:
        texto = "Nenhum produto cadastrado!!😔"
        area_produtos.insert("end", texto)

area_produtos = None

def mostrar_produtos():
    global area_produtos
    if area_produtos is None:
        area_produtos = ctk.CTkTextbox(janela, width=400, height=120)
        area_produtos.pack(pady=5)
        excluir = ctk.CTkEntry(janela,placeholder_text="ID do produto") 
        excluir.pack(pady=5)
        excluir_btn = ctk.CTkButton(janela,text="DELETAR",hover_color="red",fg_color="dark red",command=lambda: deletar_produto(excluir.get(), excluir.get()) or atualizar_graficos() or excluir.delete(0, "end"))
        excluir_btn.pack(padx=10)
        atualizar_graficos()

def cadastrar_e_atualizar():
    processar_cadastro()
    if area_produtos is not None:
        atualizar_graficos()

def criar_janela():
    global janela,lbl_mensgem,cx_nome,cx_quantidade,cx_preco

    janela = ctk.CTk()
    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()
    janela.geometry(f"{largura}x{altura}+0+0")
    janela.after(0, lambda: janela.state("zoomed"))
    janela.title("Sistema de Gestão Desktop")


    retangulo = ctk.CTkFrame(
        janela,
        width=400,
        height=1050,
        fg_color="#177277",
        corner_radius=20
    )

    retangulo.place(relx=0.5, rely=0.5, anchor="center")
    retangulo.pack_propagate(False)

    titulo = ctk.CTkLabel(retangulo,text="Sistema de Gestão Desktop",font=("arial",20),fg_color="transparent")
    titulo.pack(pady=50)

    cx_nome = ctk.CTkEntry(retangulo,placeholder_text="nome",fg_color="transparent")
    cx_nome.pack(pady=2)

    cx_quantidade = ctk.CTkEntry(retangulo,placeholder_text="quantidade",fg_color="transparent")
    cx_quantidade.pack(pady=2)

    cx_preco = ctk.CTkEntry(retangulo,placeholder_text="preço",fg_color="transparent")
    cx_preco.pack(pady=2)

    cadastrar = ctk.CTkButton(retangulo,text="CADASTRAR",hover_color="dark green",fg_color="green",command=cadastrar_e_atualizar)
    cadastrar.pack(pady=10)
    
    produtos = ctk.CTkButton(retangulo,text="VER PRODUTOS",hover_color="orange",fg_color="dark orange",command=mostrar_produtos)
    produtos.pack(pady=10)

    lbl_mensgem = ctk.CTkLabel(retangulo,text="")
    lbl_mensgem.pack()
    
    janela.mainloop()