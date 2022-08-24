"""chamando biblioteca tkinter"""
from tkinter import *


"""Definição do programa"""
master = Tk()
master.title("Sistema de Login GitHub @V3rik")
master.geometry('490x650')
master.resizable(width=False, height=False)




"""Definindo variavel global"""
esconder_senha = StringVar()




#funções
def lista_users():
    lista_tarefa = []
    cursor.execute('SELECT * FROM login')
    # row recebe as informações do banco
    row = cursor.fetchall()
    for r in row:
        lista_tarefa.append(r)
    return lista_tarefa



def nova_janela():
    """Definição do programa"""
    master1 = Tk()
    master1.title("Sistema de Login 'Dev V3rik'")
    master1.geometry('490x650')
    master1.resizable(width=False, height=False)

    # criando exibidor de dados
    listbox = Listbox(master1, font=("Courier 10 bold"), width=61, height=18)
    listbox.grid(row=1, column=0, sticky=NSEW)



    #criando variavel com lista que recebeu dadis sql:
    visualizar_dados = lista_users()
    #lop para mostrar users
    for item in visualizar_dados:
        # insert(end): insere no final da lista.
        listbox.insert(END, item)

    #executar janela
    user = cursor.execute('SELECT * FROM login')
    print(user)

    master.mainloop()





def criar_user():
    crear_email = entrada_email.get()
    crear_senha = entrada_senha.get()
    cursor.execute("INSERT INTO login VALUES('"+crear_email+"', '"+crear_senha+"')")
    banco.commit()

    cursor.execute('SELECT * FROM login')
    print(cursor.fetchall())


def deletar_user():
    deletar_email = entrada_email.get()
    deletar_senha = entrada_senha.get()
    cursor.execute("DELETE FROM login where email='"+deletar_email+"' and senha='"+deletar_senha+"' ")
    #salvar banco
    banco.commit()

    cursor.execute('SELECT * FROM login')
    print(cursor.fetchall())


def trocar_senha():
    email_da_conta = entrada_email.get()
    nova_senha = entrada_senha.get()
    cursor.execute(" update login set senha='"+nova_senha+"' where email='"+email_da_conta+"' ")
    #salvar banco
    banco.commit()



    cursor.execute('SELECT * FROM login')
    print(cursor.fetchall())






"""Importando imagens"""
img_fundo = PhotoImage(file='images/fundo.png')
img_bt_registrar = PhotoImage(file='images/criar_user.png')
img_deletar_user = PhotoImage(file='images/deletar_user.png')
img_trocar_senha = PhotoImage(file='images/alterar_senha.png')
img_ver_users = PhotoImage(file='images/ver_users.png')






""""Criando fundo"""
lab_fund = Label(master, image=img_fundo)
lab_fund.pack()



"""Criando botão criar user"""
bt_entrar = Button(master, command=criar_user,bd=0, image=img_bt_registrar)
bt_entrar.place(width=120, height=50, x=172, y=410)


"""Criando botão deletar user"""
bt_deletar_user = Button(master, command=deletar_user, bd=0, image=img_deletar_user)
bt_deletar_user.place(width=120, height=50, x=172, y=470)


"""Criando botão trocar senha"""
bt_deletar_user = Button(master, command=trocar_senha, bd=0, image=img_trocar_senha)
bt_deletar_user.place(width=120, height=50, x=172, y=530)


"""Criando botão trocar senha"""
bt_deletar_user = Button(master, command=nova_janela, bd=0, image=img_ver_users)
bt_deletar_user.place(width=120, height=50, x=172, y=590)





"""criando caixa de entrada"""
entrada_email = Entry(master, bd=2, font='Calibre 15', justify=CENTER)
entrada_email.place(width=360, height=50, x=60, y=210)
email = entrada_email.get()


entrada_senha = Entry(master, textvariable=esconder_senha, show="*", bd=2, font='Calibre 15', justify=CENTER)
entrada_senha.place(width=360, height=50, x=60, y=343)
senha = entrada_senha.get()






















#comando para baixar a biblioteca Sqlite3:
# pip install db-sqlite3

import sqlite3
#importando página main






#criando banco de dados
banco = sqlite3.connect("banco_de_dados")

#vamos criar um cursor, ele permite executar os comandos para o banco de dados.
cursor = banco.cursor()

#criando a tabela a partir do cursor:
#OBS: caso ja tenha sido executada a linha para criar a tabela irá dar erro então comente a linha.
#cursor.execute("CREATE TABLE login (email text, senha text)")



#print(criar_user())
#print((deletar_user()))
#print(trocar_senha())




#INSERINDO DADOS NO BANCO
#cursor.execute("INSERT INTO login VALUES('guilherme@gmail.com', '123456')")

#cursor.execute("INSERT INTO clientes VALUES('Agatha', 20, 'agatha@gmail.com')")










#COMANDO PARA APAGAR DADOSDO BANCO APARTIR DO NOME:
#cursor.execute("DELETE FROM clientes where nome='Guilherme'")
#cursor.execute("DELETE FROM clientes where nome='Agatha'")





#o comit confirma que estamos inserindo informações no banco
#use o nome do banco.commit
banco.commit()




#COMANDO PARA VISUALIZAR OS DADOS DO BANCO:
cursor.execute('SELECT * FROM login')
print(cursor.fetchall())
master.mainloop()
















