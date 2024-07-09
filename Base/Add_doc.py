import tkinter as tk
from tkinter import filedialog
from docx import Document

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(
        filetypes=[("Word files", "*.docx"), ("All files", "*.*")]
    )
    if caminho_arquivo:
        escrever_informacoes(caminho_arquivo)

def escrever_informacoes(caminho_arquivo):
    try:
        documento = Document(caminho_arquivo)
        # Adicionando um parágrafo com texto específico
        documento.add_paragraph("Texto adicionado pelo programa.")
        # Salvando o documento
        documento.save(caminho_arquivo)
        print(f"Informações adicionadas ao arquivo: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao abrir ou modificar o arquivo: {e}")

# Criar a janela principal
root = tk.Tk()
root.title("Selecione um arquivo Word")

# Criar um botão e associar a função selecionar_arquivo a ele
btn_selecionar = tk.Button(root, text="Selecionar arquivo", command=selecionar_arquivo)
btn_selecionar.pack(pady=20)

# Executar a interface gráfica
root.mainloop()
