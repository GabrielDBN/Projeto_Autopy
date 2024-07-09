import time
import pyautogui
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class interface_cadastro(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Software - Cadastro de inventário")
        self.geometry("400x200")

        self.login = ""
        self.senha = ""
        self.csv_path = ""

        self.home()

    def home(self):
        def csv_filedialog():
            self.csv_path = filedialog.askopenfile(filetypes= [("Tabela - csv", ".csv"), ("Todos os arquivos", "*.*")])

            if self.csv_path:
                tela_aviso = tk.Toplevel(self)
                tela_aviso.title("Aviso")
                tela_aviso.geometry("400x100")
                ttk.Label(tela_aviso, text= "Arquivo importado").pack(padx= 10, pady= 35)

            else:
                tela_aviso = tk.Toplevel(self)
                tela_aviso.title("Aviso")
                tela_aviso.geometry("400x100")
                ttk.Label(tela_aviso, text= "Erro ao importar arquivo!").pack(padx= 10, pady= 35)

        def add_automatico():
            self.login = entry_login.get()
            self.senha = entry_senha.get()
            print(f"Login: {self.login}")
            print(f"Senha: {self.senha}")

            pyautogui.PAUSE = 0.5

            pyautogui.press("win")
            pyautogui.write("firefox")
            pyautogui.press("enter")
            pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
            pyautogui.press("enter")
            time.sleep(3)

            pyautogui.click(x=680, y=510)
            pyautogui.write(self.login)
            pyautogui.press("tab") # passando pro próximo campo
            pyautogui.write(self.senha)
            pyautogui.click(x=955, y=710) # clique no botao de login
            time.sleep(3)

            tabela = pd.read_csv(self.csv_path)
            print(tabela)

            for linha in tabela.index:
                pyautogui.click(x=655, y=363)
                codigo = tabela.loc[linha, "codigo"]
                pyautogui.write(str(codigo))
                pyautogui.press("tab")
                pyautogui.write(str(tabela.loc[linha, "marca"]))
                pyautogui.press("tab")
                pyautogui.write(str(tabela.loc[linha, "tipo"]))
                pyautogui.press("tab")
                pyautogui.write(str(tabela.loc[linha, "categoria"]))
                pyautogui.press("tab")
                pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
                pyautogui.press("tab")
                pyautogui.write(str(tabela.loc[linha, "custo"]))
                pyautogui.press("tab")

                obs = tabela.loc[linha, "obs"]
                if not pd.isna(obs):
                    pyautogui.write(str(tabela.loc[linha, "obs"]))

                pyautogui.press("tab")
                pyautogui.press("enter")
                pyautogui.scroll(5000)

        label_login = ttk.Label(self, text= "Login:")
        label_login.grid(column= 0, row= 0, padx= 10, pady= 10, sticky= tk.W)
        entry_login = ttk.Entry(self, width= 25)
        entry_login.grid(column= 1, row= 0,padx= 10, pady= 10)

        label_senha = ttk.Label(self, text= "Senha:")
        label_senha.grid(column= 0, row= 1, padx= 10, pady= 10, sticky= tk.W)
        entry_senha = ttk.Entry(self, show= "*", width= 25)
        entry_senha.grid(column= 1, row= 1, padx= 10, pady= 10)

        label_arquivo = ttk.Label(self, text= "Arquivo:")
        label_arquivo.grid(column= 0, row= 2, padx= 10, pady= 10, sticky= tk.W)
        procurar_button = ttk.Button(self, text= "Procurar", command= csv_filedialog)
        procurar_button.grid(column= 1, row= 2, padx= 10, pady= 10)

        adidionar_button = ttk.Button(self, text= "Adicionar", command= add_automatico)
        adidionar_button.grid(column= 0, row= 3, padx= 10, pady= 10)
        sair_button = ttk.Button(self, text= "Sair", command= self.quit)
        sair_button.grid(column= 1, row= 3, padx= 10, pady= 10)

if __name__ == "__main__":
    app = interface_cadastro()
    app.mainloop()