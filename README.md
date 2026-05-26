# Sistema de Gestão Desktop

Sistema de gerenciamento de produtos desenvolvido em Python utilizando arquitetura MVC, interface moderna com CustomTkinter e dashboard gráfico com Matplotlib.

---

## Funcionalidades

* Cadastro de produtos
* Atualização de produtos
* Exclusão de produtos
* Listagem dinâmica de produtos
* Dashboard com gráficos
* Interface moderna
* GIF animado de fundo
* Navegação por Enter entre campos
* Sistema compilado para `.exe`

---

## Tecnologias Utilizadas

* Python
* CustomTkinter
* SQLite3
* Matplotlib
* Pillow (PIL)
* PyInstaller

---

## Arquitetura do Projeto

O projeto foi organizado utilizando o padrão MVC:

* `tela.py` → Interface gráfica
* `controlador.py` → Regras e validações
* `modelo.py` → Banco de dados SQLite

---

## Como Executar

### Instalar dependências

```bash
pip install customtkinter matplotlib pillow
```

### Executar projeto

```bash
python main.py
```

---

## Executável

O projeto também pode ser compilado para `.exe` utilizando:

```bash
python -m PyInstaller --onefile --windowed --icon=icone.ico --add-data "fundo.gif;." main.py
```

---

## Interface

O sistema possui:

* Tema escuro moderno
* Componentes estilizados
* Dashboard interativo
* Gráficos personalizados
* Interface inspirada em dashboards modernos

---

## Autor

Desenvolvido por pietro
