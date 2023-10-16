# import tkinter

# janela = tkinter.Tk()
# janela.geometry("500x300")



# texto = tkinter.Label(janela, text="Fazer Login")
# texto.pack(padx=10, pady=10)

# botao = tkinter.Button(janela, text="Login")
# botao.pack(padx=10 ,pady=10)

# janela.mainloop()

def clique():
  print("Fazer Login")

import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

check = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
check.pack(padx=10, pady=10)


botao = customtkinter.CTkButton(janela, text="Login", command=clique)  # Corrigido aqui
botao.pack(padx=10, pady=10)



janela.mainloop()
