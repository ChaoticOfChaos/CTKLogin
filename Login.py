from customtkinter import *
import pandas as pd

data = pd.read_excel('Data-bank.xlsx')

def entrar():
    email = entrada_email.get()
    senha = entrada_senha.get()
    if email in data['email'].tolist():
        if senha in data['senha'].tolist():
            top = CTkToplevel()
        else:
            acao.configure(text='Senha Inválida')
    else:
        acao.configure(text='E-mail Inválido')

def criar():
    def fazer():
        nome = entrada_nome.get()
        novo_email = entrada_novo_email.get()
        nova_senha = entrada_nova_senha.get()
        username = entrada_user_name.get()
        seletor_pais = pais.get()
        data.loc['email'] = novo_email, nova_senha, nome, username, seletor_pais
        data.to_excel('Data-bank.xlsx', index=False)
        top.destroy()

    top = CTkToplevel()
    top.title('Cadastrar-se')
    top.geometry('350x350')

    top_frame = CTkFrame(top)
    top_frame.pack(padx=60, pady=20, fill='both', expand=True)

    entrada_nome = CTkEntry(top_frame, placeholder_text='Insira seu Nome')
    entrada_nome.pack(padx=10, pady=12)

    entrada_novo_email = CTkEntry(top_frame, placeholder_text='Insira seu E-mail')
    entrada_novo_email.pack(padx=10, pady=12)

    entrada_nova_senha = CTkEntry(top_frame, placeholder_text='Insira sua Senha')
    entrada_nova_senha.pack(padx=10, pady=12)

    entrada_user_name = CTkEntry(top_frame, placeholder_text='Insira seu UserName')
    entrada_user_name.pack(padx=10, pady=12)

    pais = CTkOptionMenu(top_frame, values=['Brasil', 'USA', 'Mexico', 'Canada', 'Argentina', 'Portugal', 'Germany', 'Russia', 'China', 'Poland'])
    pais.pack(padx=10, pady=12)

    botao_afirmar = CTkButton(top_frame, text='Criar Conta', command=fazer)
    botao_afirmar.pack(padx=10, pady=12)

root = CTk()
root.title('KSLogin-System')
root.geometry('300x400')

frame = CTkFrame(root)
frame.pack(padx=60, pady=20, fill='both', expand=True)

entrada_email = CTkEntry(frame, placeholder_text='Insira o seu E-mail')
entrada_email.pack(padx=10, pady=12)

entrada_senha = CTkEntry(frame, placeholder_text='Insira a sua Senha')
entrada_senha.pack(padx=10, pady=12)

botao_confirmar = CTkButton(frame, text='Login', command=entrar)
botao_confirmar.pack(padx=10, pady=12)

botao_criar = CTkButton(frame, text='Cadastre-se', command=criar)
botao_criar.pack(padx=10, pady=12)

acao = CTkLabel(root, text='')
acao.pack()

root.mainloop()