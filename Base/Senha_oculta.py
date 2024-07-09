import tkinter as tk

# Função para ser chamada quando o botão de login for pressionado
def login():
    print("Senha:", entry.get())

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Campo de Senha")

# Criação de um label para o campo de senha
label = tk.Label(root, text="Senha:")
label.pack(pady=5)

# Criação do campo de entrada de senha, com a opção show configurada para ocultar os caracteres
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

# Criação de um botão de login
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Execução da janela principal
root.mainloop()
