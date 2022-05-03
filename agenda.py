import os
import sys
import string
import sqlite3

def UserChoose():
 
    os.system("cls");
    print ("===================================")
    print ("======= Agenda de Contatos ========")
    print ("===================================")
    print ("Escolha a alternativa desejada: ")
    print ("1 - Criar banco de dados")
    print ("2 - Cadastrar")
    print ("3 - Alterar")
    print ("4 - Consultar")
    print ("5 - Excluir")
    print ("6 - Mostrar Todos")
    print ("7 - Sair")

    choose = input("Digite aqui: ")
 
    if choose == '1':
        cria_banco() 
    
    elif choose == '2':
        Cadastrar()

    elif choose == '3':
        Alterar()
 
    elif choose == '4':
        Consultar()
 
    elif choose == '5':
        Excluir()       
    
    elif choose == '6':
        MostrarTodos()
 
    elif choose == '7':
        sys.exit()

    else:
        print ("Escolha uma das alternativas acima!")
        UserChoose()

def cria_banco():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Contatos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR NOT NULL, telefone VARCHAR NOT NULL)""");
    conn.close()
    UserChoose()

def Cadastrar():
    a = input("Digite o nome do contato: ")
    b = input("Digite o telefone do contato: ")
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Contatos(nome, telefone) VALUES(?, ?) """, (a, b))
    conn.commit()
    c = input("Digite 8 para encerrar a cadastro e voltar ao menu ou qualquer coisa para encerrar o programa: ")
    if c == '8':
        conn.close()
        UserChoose()
    else:
        conn.close()
        sys.exit()

def Alterar():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()

    id_contato = int(input("Digite o ID do contato: "))
    novo_fone = input("Digite o novo telefone: ")
    cursor.execute("""UPDATE Contatos SET telefone = ? WHERE id = ?""", (novo_fone, id_contato))
    conn.commit()
    c = input("Digite 8 para encerrar a alteração e voltar ao menu ou qualquer coisa para encerrar o programa: ")
    if c == '8':
        conn.close()
        UserChoose()
    else:
        conn.close()
        sys.exit()

def Consultar():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    nome_busca = input("Digite o id a ser consultado: ")

    cursor.execute("""SELECT * FROM Contatos WHERE id = ?""", (nome_busca))
    for linha in cursor.fetchall():
        print("ID: ", linha[0])
        print("Nome: ", linha[1])
        print("Telefone: ", linha[2])
    c = input("Digite 8 para encerrar a consulta e voltar ao menu ou qualquer coisa para encerrar o programa: ")
    if c == '8':
        conn.close()
        UserChoose()
    else:
        conn.close()
        sys.exit() 

def Excluir():
  
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    id_contato = input("Digite o id do contato: ")
    cursor.execute("""DELETE FROM Contatos WHERE id = ?""", (id_contato))
    conn.commit()
    c = input("Digite 8 para encerrar a consulta e voltar ao menu ou qualquer coisa para encerrar o programa: ")
    if c == '8':
        conn.close()
        UserChoose()
    else:
        conn.close()
        sys.exit() 

def MostrarTodos():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Contatos;""")

    for linha in cursor.fetchall():
        print("ID: ", linha[0])
        print("Nome: ", linha[1])
        print("Telefone: ", linha[2])
    c = input("Digite 8 para encerrar a consulta e voltar ao menu ou qualquer coisa para encerrar o programa: ")
    if c == '8':
        conn.close()
        UserChoose()
    else:
        conn.close()
        sys.exit() 


if __name__=='__main__':
    UserChoose()
