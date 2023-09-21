import tkinter as tk
from tkinter import Scrollbar, filedialog, Text, Menu, messagebox

def abrir_arquivo():
    # Solicitar ao usuário para selecionar um arquivo
    arquivo=filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])

    if arquivo:
        # Limpar qualquer conteúdo existente na caixa de texto
        caixa_texto.delete("1.0", tk.END)

        # Abrir o arquivo e ler seu conteúdo
        with open(arquivo, "r", encoding="utf-8") as file:
            conteudo=file.read()
        # Inserir o conteúdo do arquivo na caixa de texto
        caixa_texto.insert(tk.END, conteudo)

def salvar():
    texto_digitado=caixa_texto.get()

    nome_arquivo=filedialog.asksaveasfilename(filetypes=[("Arquivos de Texto","*.txt")])
    
    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(texto_digitado+"\n")
    # entrada_texto.delete(0, tk.END)
    messagebox.showinfo("Confirmação","Arquivo com sucesso!")

def sair():
    janela.quit()

# Função para add texto à caixa de texto
def adicionar_texto():
    texto = "Olá Mundo"
    caixa_texto.insert(tk.END, texto + "\n")

# Cria uma janela
janela = tk.Tk()
janela.title("Leitor de arquivos")

#Cria uma barra de menu
barra_menu=Menu(janela)
janela.config(menu=barra_menu)

# Cria um menu "Arquivo" com subitens
menu_arquivo = Menu(barra_menu)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar)
menu_arquivo.add_separator() # Separador entre os itens
menu_arquivo.add_command(label="Sair",command=sair)

#Cria uma barra de rolagem vertical
barra_rolagem = Scrollbar(janela)
barra_rolagem.pack(side=tk.RIGHT, fill=tk.Y)

# Cria uma caixa de texto com barra de rolagem
caixa_texto = Text(janela, wrap=tk.WORD, yscrollcommand=barra_rolagem.set)
caixa_texto.pack(fill=tk.BOTH)
barra_rolagem.config(command=caixa_texto.yview)

# Cria um botão para adicionar texto à caixa de texto
botao_adicionar = tk.Button(janela, text="Ler arquivo", command=abrir_arquivo)
botao_adicionar.pack()

# Inicia a interface gráfica
janela.mainloop()