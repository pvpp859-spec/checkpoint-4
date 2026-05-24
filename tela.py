import customtkinter as ctk
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from controlador import processar_cadastro
from modelo import buscar_produto, deletar_produto,atualizar_produto
from PIL import Image,ImageTk,ImageSequence
janela_edicao = None
janela_graficos = None
area_produtos = None
#janela de edição
def abrir_edicao(produto):
    global janela_edicao,salvar_edicao,cx_nome_edi,cx_quantidade_edi,cx_preco_edi
    if janela_edicao is not None:
        janela_edicao.destroy()

    janela_edicao = ctk.CTkToplevel(janela)

    largura = 500
    altura = 400

    x = (janela_edicao.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela_edicao.winfo_screenheight() // 2) - (altura // 2)

    janela_edicao.geometry(f"{largura}x{altura}+{x}+{y-30}")
    janela_edicao.title("Editar Produto")
    janela_edicao.transient(janela_graficos)
    id_produto = produto[0]
    cx_titulo = ctk.CTkLabel(janela_edicao, text=f"Editando Produto ID: {produto[1]}", font=("Arial", 18, "bold"))
    cx_titulo.pack(pady=20)
    cx_nome_edi = ctk.CTkEntry(janela_edicao, placeholder_text="nome")
    cx_nome_edi.pack(pady=10)
    cx_nome_edi.insert(0, produto[1])

    cx_quantidade_edi = ctk.CTkEntry(janela_edicao, placeholder_text="quantidade")
    cx_quantidade_edi.pack(pady=10)
    cx_quantidade_edi.insert(0, produto[2])

    cx_preco_edi = ctk.CTkEntry(janela_edicao, placeholder_text="preço")
    cx_preco_edi.pack(pady=10)
    cx_preco_edi.insert(0, produto[3])

    cx_nome_edi.bind("<Return>",lambda event: enter("nome"))
    cx_quantidade_edi.bind("<Return>",lambda event: enter("quantidade"))
    cx_preco_edi.bind("<Return>",lambda event: enter("preço"))

    def salvar_edicao():
        atualizar_produto(
            id_produto,
            cx_nome_edi.get(),
            int(cx_quantidade_edi.get()),
            float(cx_preco_edi.get())
        )

        janela_edicao.destroy()
        atualizar_lista_produtos()

    btn_salvar = ctk.CTkButton(janela_edicao,text="SALVAR",command=salvar_edicao)
    btn_salvar.pack(pady=20)
#atulizar e deletar produtos
def atualizar_lista_produtos():
    for widget in area_produtos.winfo_children():
        widget.destroy()
    produtos = buscar_produto()
    for produto in produtos:
        id_produto = produto[0]
        linha = ctk.CTkFrame(area_produtos, fg_color="#020916")
        linha.pack(fill="x", padx=10, pady=5)
        texto = f"ID: {produto[0]} | Produto: {produto[1]} | Quantidade: {produto[2]} | Preço: R${produto[3]}"
        lbl = ctk.CTkLabel(linha,text=texto,font=("Arial", 18),text_color="white")
        lbl.pack(side="left", padx=10, pady=10)
        btn_atualizar = ctk.CTkButton(linha,text="ATUALIZAR",width=120,fg_color="orange",command=lambda p=produto: abrir_edicao(p))
        btn_atualizar.pack(side="right", padx=5)
        btn_excluir = ctk.CTkButton(linha,text="EXCLUIR",width=120,fg_color="dark red",hover_color="red",command=lambda id=id_produto: deletar_e_atualizar(id))
        btn_excluir.pack(side="right", padx=5)
#função para deletar e atualizar a lista de produtos
def deletar_e_atualizar(id_produto):
    deletar_produto(id_produto)
    atualizar_lista_produtos()
#gif de fundo
def animar_gif(indice):
    frame = frames[indice]
    label_gif.configure(image=frame)
    indice +=1
    if indice >= len(frames):
        indice = 0
    janela.after(50,lambda:animar_gif(indice))
#gerar dashboard com gráficos
def abrir_dashboard():
    janela_dashboard = ctk.CTkToplevel(janela)
    janela_dashboard.title("Dashboard")
    janela_dashboard.geometry("900x600")
    janela_dashboard.transient(janela_graficos)

    produtos = buscar_produto()

    nomes = []
    quantidades = []

    for produto in produtos:
        nomes.append(produto[1])
        quantidades.append(produto[2])

    figura = Figure(figsize=(8, 5), dpi=100)
    grafico = figura.add_subplot(111)

    grafico.bar(nomes, quantidades)
    grafico.set_title("Quantidade por Produto")
    grafico.set_xlabel("Produtos")
    grafico.set_ylabel("Quantidade")

    canvas = FigureCanvasTkAgg(figura, master=janela_dashboard)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)
#trocar tela
def fechar_janela():
    global janela_graficos,area_produtos
    janela_graficos.destroy()
    janela_graficos = None
    area_produtos = None
#abrir janela
def abrir_janela():
    global janela_graficos
    if janela_graficos is None:
        janela_graficos = ctk.CTkToplevel(janela)
        janela_graficos.geometry(f"{largura}x{altura}+0+0")
        janela_graficos.after(0, lambda: janela.state("zoomed"))
        janela_graficos.after(0,lambda:janela_graficos.state("zoomed"))
        janela_graficos.transient(janela)
        janela_graficos.protocol("WM_DELETE_WINDOW",fechar_janela)
#lista de produtos
def atualizar_graficos():
    area_produtos.delete("0.0","end")
    produtos = buscar_produto()
    for produto in produtos:
        texto = f"ID: {produto[0]} - Produto: {produto[1]} - Quantidade: {produto[2]} - Preço: {produto[3]}R$\n"
        area_produtos.insert("end", texto)
    if len(produtos) == 0:
        area_produtos.insert("end", texto)     
#clicou enter
def enter(campo):

    # JANELA PRINCIPAL
    if janela_edicao is None:

        if campo == "nome":
            if cx_nome.get() == "":
                lbl_mensgem.configure(
                    text="digite o nome do produto!!",
                    text_color="red"
                )
            else:
                lbl_mensgem.configure(text="")
                cx_quantidade.focus()

        elif campo == "quantidade":
            if cx_quantidade.get() == "":
                lbl_mensgem.configure(
                    text="digite a quantidade!!",
                    text_color="red"
                )
            else:
                lbl_mensgem.configure(text="")
                cx_preco.focus()

        elif campo == "preço":
            if cx_preco.get() == "":
                lbl_mensgem.configure(
                    text="digite o preço!!",
                    text_color="red"
                )
            else:
                lbl_mensgem.configure(text="")
                cadastrar_e_atualizar()

    # JANELA DE EDIÇÃO
    else:

        if campo == "nome":
            cx_quantidade_edi.focus()

        elif campo == "quantidade":
            cx_preco_edi.focus()

        elif campo == "preço":
            salvar_edicao()   
#mostrar a tabela de produtos
def mostrar_produtos():
    global area_produtos
    #abrir outra janela
    abrir_janela()
    #criar area para os produtos
    janela_graficos.configure(fg_color="#0F172A")
    if area_produtos is None:
        titulo = ctk.CTkLabel(janela_graficos,text="TABELA DE PRODUTOS",text_color="white",font=("arial",18,"bold"))
        titulo.pack(pady=20)
        area_produtos = ctk.CTkScrollableFrame(janela_graficos,width=1500,height=700,fg_color="#F9FBFD")
        area_produtos.pack(pady=10)
        dashbord = ctk.CTkButton(janela_graficos,text="GRAFICOS",hover_color="red",fg_color="dark red",command=lambda: abrir_dashboard(),width=250,height=35)
        dashbord.pack(pady=20)
        voltar = ctk.CTkButton(janela_graficos,text="VOLTAR",fg_color="dark green",hover_color="green",command=fechar_janela,height=35,width=250)
        voltar.pack(pady=10)
        atualizar_lista_produtos()
#cadastrar e atualizar a lista de produtos
def cadastrar_e_atualizar():
    processar_cadastro()
    if area_produtos is not None:
        atualizar_graficos()
#criar a janela principal
def criar_janela():
    global janela,lbl_mensgem,cx_nome,cx_quantidade,cx_preco,retangulo,altura,largura,frames,label_gif

    janela = ctk.CTk()
    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()
    janela.geometry(f"{largura}x{altura}+0+0")
    janela.after(0, lambda: janela.state("zoomed"))
    janela.title("Sistema de Gestão Desktop")

    gif = Image.open("fundo.gif")

    frames = []
    contador = 0

    for frame in ImageSequence.Iterator(gif):
        if contador >= 100:
            break
        frame = frame.copy()
        frame = frame.resize((largura, altura),Image.Resampling.LANCZOS)
        frames.append(ImageTk.PhotoImage(frame))
        contador += 1

    label_gif = ctk.CTkLabel(janela,text="",image=frames[0])
    label_gif.place(x=0,y=0)
    label_gif.lower()
    animar_gif(0)  

    retangulo = ctk.CTkFrame(janela,width=400,height=1050,fg_color="#177277",corner_radius=20)

    retangulo.place(relx=0.5, rely=0.5, anchor="center")
    retangulo.pack_propagate(False)

    titulo = ctk.CTkLabel(retangulo,text="Sistema de Gestão Desktop",text_color="white",font=("arial",20),fg_color="transparent")
    titulo.pack(pady=50)

    cx_nome = ctk.CTkEntry(retangulo,placeholder_text="nome",placeholder_text_color="white",fg_color="transparent")
    cx_nome.pack(pady=2)

    cx_quantidade = ctk.CTkEntry(retangulo,placeholder_text="quantidade",placeholder_text_color="white",fg_color="transparent")
    cx_quantidade.pack(pady=2)

    cx_preco = ctk.CTkEntry(retangulo,placeholder_text="preço",placeholder_text_color="white",fg_color="transparent")
    cx_preco.pack(pady=2)

    cadastrar = ctk.CTkButton(retangulo,text="CADASTRAR",hover_color="dark green",fg_color="green",command=cadastrar_e_atualizar)
    cadastrar.pack(pady=10)
    
    produtos = ctk.CTkButton(retangulo,text="VER PRODUTOS",hover_color="orange",fg_color="dark orange",command=mostrar_produtos)
    produtos.pack(pady=10)

    lbl_mensgem = ctk.CTkLabel(retangulo,text="")
    lbl_mensgem.pack()

    cx_nome.bind("<Return>",lambda event: enter("nome"))
    cx_quantidade.bind("<Return>",lambda event: enter("quantidade"))
    cx_preco.bind("<Return>",lambda event: enter("preço"))

    janela.mainloop()