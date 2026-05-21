import customtkinter as ctk
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from modelo import buscar_produto

def gerar_graficos():
    graficos = ctk.CTkButton(janela,text="GRAFICO")
    graficos.pack(pady=10)
    

def criar_janela():
    global janela,lbl_mensgem

    janela = ctk.CTk()
    janela.geometry("550x500")
    janela.title("Sistema de Gestão Desktop")

    titulo = ctk.CTkLabel(janela,text="Sistema de Gestão Desktop",font=("arial",20))
    titulo.pack(pady=20)

    cx_nome = ctk.CTkEntry(janela,placeholder_text="nome")
    cx_nome.pack(pady=2)

    cx_quantidade = ctk.CTkEntry(janela,placeholder_text="quantidade")
    cx_quantidade.pack(pady=2)

    cx_preco = ctk.CTkEntry(janela,placeholder_text="preço")
    cx_preco.pack(pady=2)

    cadastrar = ctk.CTkButton(janela,text="CADASTRAR",hover_color="dark green",fg_color="green")
    cadastrar.pack(pady=10)

    produtos = ctk.CTkButton(janela,text="VER PRODUTOS",hover_color="orange",fg_color="dark orange")
    produtos.pack(pady=10)

    lbl_mensgem = ctk.CTkLabel(janela,text="")
    lbl_mensgem.pack()

    janela.mainloop()