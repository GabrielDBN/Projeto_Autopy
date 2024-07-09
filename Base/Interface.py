import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exemplo de Interface com Labels e Caixas de Texto")
        self.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        # Label e Caixa de Texto para Nome
        self.label_nome = ttk.Label(self, text="Nome:")
        self.label_nome.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
        
        self.entry_nome = ttk.Entry(self, width=30)
        self.entry_nome.grid(column=1, row=0, padx=10, pady=10)

        # Label e Caixa de Texto para Idade
        self.label_idade = ttk.Label(self, text="Idade:")
        self.label_idade.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
        
        self.entry_idade = ttk.Entry(self, width=30)
        self.entry_idade.grid(column=1, row=1, padx=10, pady=10)

        # Label e Caixa de Texto para Email
        self.label_email = ttk.Label(self, text="Email:")
        self.label_email.grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
        
        self.entry_email = ttk.Entry(self, width=30)
        self.entry_email.grid(column=1, row=2, padx=10, pady=10)

        # Botão para Submeter
        self.submit_button = ttk.Button(self, text="Submeter", command=self.submit)
        self.submit_button.grid(column=1, row=3, padx=10, pady=20)

    def submit(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        email = self.entry_email.get()
        print(f"Nome: {nome}, Idade: {idade}, Email: {email}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
